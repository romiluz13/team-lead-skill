"""Local action environment. Scenario expectations are never passed to it."""
import copy
import json
import random
from pathlib import Path


class Environment:
    def __init__(self, root, initial, seed):
        self.root = Path(root).resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self.state = copy.deepcopy(initial.get('state', {}))
        self.events = []
        self.rng = random.Random(seed)
        for name, content in initial.get('files', {}).items():
            self.write(name, content)

    def path(self, name):
        path = (self.root / name).resolve()
        if not path.is_relative_to(self.root) or path == self.root:
            raise ValueError('path outside disposable root')
        return path

    def write(self, name, content):
        path = self.path(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)

    def event(self, kind, **data):
        self.events.append({'tick': len(self.events), 'kind': kind, **data})

    def apply(self, action, actor='lead'):
        op = action['op']
        self.event(op, actor=actor, **{k: v for k, v in action.items() if k != 'op'})
        if op == 'write':
            self.write(action['path'], action['content'])
        elif op == 'read':
            self.event('read_result', actor=actor, path=action['path'],
                       content=self.path(action['path']).read_text())
        elif op == 'set':
            self.state[action['key']] = copy.deepcopy(action['value'])
        elif op == 'submit':
            self.state.setdefault('submissions', []).append(action['attempt'])
        elif op == 'delivery':
            self.state.setdefault('delivered', []).append({'attempt': action['attempt'], 'session': action['session']})
        elif op == 'ack':
            self.state.setdefault('acknowledged', []).append(action['attempt'])
        elif op == 'return':
            self.write(action['path'], json.dumps(action['result'], sort_keys=True))
            self.event('return_persisted', attempt=action['attempt'], path=action['path'])
        elif op == 'accept':
            result = json.loads(self.path(action['path']).read_text())
            self.state.setdefault('accepted', []).append(result)
            self.event('accepted_result', result=result)
        elif op == 'notify':
            self.event('notification_result', status='blocked' if self.state.get('lead_status') == 'blocked' else 'submitted')
        elif op == 'delete':
            self.path(action['path']).unlink()
        elif op == 'spawn':
            self.state['children'] = self.state.get('children', 0) + 1
        elif op == 'mutate':
            self.write(action['path'], action['content'])
        elif op == 'restart':
            self.state['lead_session'] = action['session']
            self.state.pop('volatile', None)
        elif op == 'interrupt':
            self.state.setdefault('workers', {})[action['target']] = 'idle'
            self.event('interrupt_ack', target=action['target'])
        elif op == 'worker_step':
            if self.state.get('workers', {}).get(action['target']) == 'working':
                self.write(action['path'], action['content'])
                self.event('worker_write', target=action['target'], path=action['path'])
        elif op == 'inspect':
            self.event('inspection_result', target=action['target'], state=copy.deepcopy(self.state))
        elif op not in {'inspect', 'hold', 'interrupt', 'wait', 'check', 'decision'}:
            raise ValueError(f'unknown operation: {op}')

    def inject(self, injections):
        for injection in injections:
            actions = list(injection['actions'])
            if injection.get('shuffle'):
                self.rng.shuffle(actions)
            for action in actions:
                self.apply(action, actor='environment')

    def snapshot(self):
        files = {str(p.relative_to(self.root)): p.read_text()
                 for p in sorted(self.root.rglob('*')) if p.is_file() and self.path(str(p.relative_to(self.root)))}
        return {'state': self.state, 'files': files, 'events': self.events}


def grade(snapshot, invariants):
    failures = []
    for rule in invariants:
        kind = rule['kind']
        events = snapshot['events']
        if kind == 'state':
            ok = snapshot['state'].get(rule['key']) == rule['value']
            if rule['key'] == 'accepted':
                observed = [e['result'] for e in events if e['kind'] == 'accepted_result']
                ok = ok and observed == rule['value'] and not any(
                    e['kind'] == 'set' and e.get('key') == 'accepted' for e in events)
        elif kind == 'file':
            ok = snapshot['files'].get(rule['path']) == rule['content']
        elif kind == 'event':
            ok = any(all(e.get(k) == v for k, v in rule['match'].items()) for e in events)
        elif kind == 'absent':
            ok = not any(all(e.get(k) == v for k, v in rule['match'].items()) for e in events)
        elif kind == 'before':
            positions = [[e['tick'] for e in events if all(e.get(k) == v for k, v in match.items())]
                         for match in (rule['first'], rule['second'])]
            ok = bool(positions[0] and positions[1]) and max(positions[0]) < min(positions[1])
        elif kind == 'count':
            ok = sum(all(e.get(k) == v for k, v in rule['match'].items()) for e in events) == rule['value']
        else:
            raise ValueError(f'unknown invariant: {kind}')
        if not ok:
            failures.append(rule['name'])
    return failures
