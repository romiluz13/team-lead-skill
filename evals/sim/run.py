import argparse
import json
import tempfile
from pathlib import Path
from engine import Environment, grade


def run(seed, variant='both'):
    base = Path(__file__).resolve().parent
    scenarios = json.loads((base / 'scenarios.json').read_text())
    scripts = json.loads((base / 'scripts.json').read_text())
    results = []
    with tempfile.TemporaryDirectory(prefix='run-', dir=base) as temporary:
        for case in scenarios:
            for lead in ('correct', 'broken') if variant == 'both' else (variant,):
                env = Environment(Path(temporary) / case['id'] / lead, case['initial'], seed)
                execution_error = None
                try:
                    for phase in scripts[case['id']][lead]:
                        if phase == 'inject':
                            env.inject(case['injections'])
                        else:
                            env.apply(phase)
                except (ValueError, OSError, KeyError, TypeError) as error:
                    execution_error = f'{type(error).__name__}: {error}'
                snapshot = env.snapshot()
                evidence = Path(temporary) / case['id'] / f'{lead}-evidence.json'
                evidence.write_text(json.dumps(snapshot, sort_keys=True))
                snapshot = json.loads(evidence.read_text())
                failures = grade(snapshot, case['invariants'])
                if execution_error:
                    failures.append(execution_error)
                results.append({'scenario': case['id'], 'lead': lead,
                                'passed': not failures, 'execution_error': execution_error, 'failures': failures, 'snapshot': snapshot})
    return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', type=int, default=23)
    parser.add_argument('--lead', choices=['both', 'correct', 'broken'], default='both')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    results = run(args.seed, args.lead)
    for result in results:
        print(f"{result['scenario']:26} {result['lead']:7} {'PASS' if result['passed'] else 'FAIL'}" +
              (f" [{', '.join(result['failures'])}]" if result['failures'] else ''))
    if args.report:
        base = Path(__file__).resolve().parent
        report = args.report.resolve()
        if not report.is_relative_to(base) or report == base:
            parser.error('--report must be inside sim/')
        report.write_text(json.dumps({'seed': args.seed, 'results': results}, indent=2, sort_keys=True) + '\n')
    valid = all(r['passed'] == (r['lead'] == 'correct') for r in results) if args.lead == 'both' else all(r['passed'] for r in results)
    valid = valid and not any(r['execution_error'] for r in results)
    print(('DISCRIMINANCE PASS' if args.lead == 'both' else 'SELECTED LEAD PASS') if valid else 'VALIDATION FAIL')
    raise SystemExit(0 if valid else 1)
