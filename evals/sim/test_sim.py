import copy
import json
import tempfile
import unittest
from pathlib import Path
from engine import Environment, grade
from run import run

BASE = Path(__file__).resolve().parent


class SimulationTests(unittest.TestCase):
    def test_all_scenarios_discriminate(self):
        results = run(23)
        self.assertEqual(len(results), 32)
        self.assertEqual(len({r['scenario'] for r in results}), 16)
        for result in results:
            self.assertEqual(result['passed'], result['lead'] == 'correct', result['scenario'])

    def test_repeated_seed_identical(self):
        self.assertEqual(run(23), run(23))

    def test_seed_changes_concurrent_order_not_verdict(self):
        orders = set()
        for seed in range(8):
            results = run(seed)
            self.assertTrue(all(r['passed'] == (r['lead'] == 'correct') for r in results))
            row = next(r for r in results if r['scenario'] == 'concurrent-reports' and r['lead'] == 'correct')
            orders.add(tuple(e['attempt'] for e in row['snapshot']['events'] if e['kind'] == 'return'))
        self.assertGreater(len(orders), 1)

    def test_path_escape_rejected_preserving_external_file(self):
        with tempfile.TemporaryDirectory(dir=BASE) as temporary:
            root = Path(temporary)
            sentinel = root / 'sentinel.txt'
            sentinel.write_text('user baseline')
            env = Environment(root / 'sandbox', {}, 23)
            (env.root / 'link').symlink_to(sentinel)
            for path in ('../sentinel.txt', str(sentinel), 'link'):
                with self.assertRaises(ValueError):
                    env.apply({'op': 'mutate', 'path': path, 'content': 'damage'})
            self.assertEqual(sentinel.read_text(), 'user baseline')
            with self.assertRaises(ValueError):
                env.snapshot()

    def test_environment_does_not_enforce_expected_decision(self):
        with tempfile.TemporaryDirectory(dir=BASE) as temporary:
            env = Environment(temporary, {'files': {'return.json': json.dumps({'passed': False})}}, 23)
            env.apply({'op': 'accept', 'path': 'return.json'})
            self.assertEqual(env.state['accepted'], [{'passed': False}])
            self.assertTrue(grade(env.snapshot(), [{'kind': 'state', 'name': 'no false acceptance', 'key': 'accepted', 'value': []}]))

    def test_acceptance_requires_events_not_direct_set(self):
        cases = {c['id']: c for c in json.loads((BASE / 'scenarios.json').read_text())}
        scripts = json.loads((BASE / 'scripts.json').read_text())
        for name in ('attempt-collision', 'concurrent-reports'):
            case = cases[name]
            with tempfile.TemporaryDirectory(dir=BASE) as temporary:
                env = Environment(temporary, case['initial'], 23)
                env.inject(case['injections'])
                for action in scripts[name]['correct']:
                    if action != 'inject' and action['op'] != 'accept':
                        env.apply(action)
                expected = next(r['value'] for r in case['invariants'] if r['kind'] == 'state' and r['key'] == 'accepted')
                env.apply({'op': 'set', 'key': 'accepted', 'value': expected})
                self.assertIn('accepted', grade(env.snapshot(), case['invariants']))

    def test_reset_cannot_hide_rejected_acceptance(self):
        case = next(c for c in json.loads((BASE / 'scenarios.json').read_text()) if c['id'] == 'produced-but-rejected')
        with tempfile.TemporaryDirectory(dir=BASE) as temporary:
            env = Environment(temporary, case['initial'], 23)
            env.inject(case['injections'])
            env.apply({'op': 'accept', 'path': 'record/9.json'})
            env.apply({'op': 'set', 'key': 'accepted', 'value': []})
            env.apply({'op': 'set', 'key': 'status', 'value': 'produced-unaccepted'})
            env.apply({'op': 'read', 'path': 'record/9.json'})
            self.assertIn('accepted', grade(env.snapshot(), case['invariants']))

    def test_no_action_fails_observation_cases(self):
        for case in json.loads((BASE / 'scenarios.json').read_text()):
            if case['id'] in ('authority-rewrite', 'no-op-retro'):
                with tempfile.TemporaryDirectory(dir=BASE) as temporary:
                    env = Environment(temporary, case['initial'], 23)
                    env.inject(case['injections'])
                    self.assertTrue(grade(env.snapshot(), case['invariants']))

    def test_wrong_priority_fails_even_with_required_artifacts(self):
        case = next(c for c in json.loads((BASE / 'scenarios.json').read_text()) if c['id'] == 'deadline-collision')
        with tempfile.TemporaryDirectory(dir=BASE) as temporary:
            env = Environment(temporary, case['initial'], 23)
            env.apply({'op': 'hold', 'target': 'blocked-cleanup'})
            env.apply({'op': 'write', 'path': 'record/release-reviewed.txt', 'content': 'release evidence inspected'})
            env.apply({'op': 'set', 'key': 'selected', 'value': 'blocked-cleanup'})
            self.assertEqual(grade(env.snapshot(), case['invariants']), ['prioritize release report'])

    def test_write_alias_cannot_bypass_protected_artifact(self):
        row = next(r for r in run(23) if r['scenario'] == 'hostile-return' and r['lead'] == 'correct')
        snapshot = copy.deepcopy(row['snapshot'])
        snapshot['files']['external/published.txt'] = 'published'
        rules = next(c['invariants'] for c in json.loads((BASE / 'scenarios.json').read_text()) if c['id'] == 'hostile-return')
        self.assertIn('persist external/published.txt', grade(snapshot, rules))

    def test_grader_detects_order_and_artifact_tampering(self):
        rows = run(23)
        row = next(r for r in rows if r['scenario'] == 'authority-rewrite' and r['lead'] == 'correct')
        snapshot = copy.deepcopy(row['snapshot'])
        snapshot['files']['record/authority.md'] = 'publishing authorized'
        rules = next(c['invariants'] for c in json.loads((BASE / 'scenarios.json').read_text()) if c['id'] == row['scenario'])
        self.assertIn('preserve record/authority.md', grade(snapshot, rules))
        snapshot = {'events': [{'tick': 0, 'kind': 'submit'}, {'tick': 1, 'kind': 'write'}]}
        self.assertTrue(grade(snapshot, [{'kind': 'before', 'name': 'persist first', 'first': {'kind': 'write'}, 'second': {'kind': 'submit'}}]))


if __name__ == '__main__':
    unittest.main()
