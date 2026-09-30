# Executed simulation: scripted validation

Run from any directory, without dependencies or network:

```sh
/path/to/evals/sim/run.sh --seed 23
```

Default runs both scripted leads for all 16 scenarios. Exit 0 means every correct script passes and every broken script fails. A broken FAIL is expected evidence of discrimination, not a suite failure. `--lead correct` and `--lead broken` return conventional status: exit 0 only if all selected scripts pass; the broken suite exits 1. Optional `--report /absolute/path/inside/sim/report.json` persists full events, final files, state, and invariant failures. Reports may only be written inside sim/.

`scenarios.json` contains facts, initial files/state, seeded fault schedules and observable invariants. `scripts.json` contains independent action sequences for correct/broken leads. `engine.py` has no scenario IDs, expected outcomes, or access to invariants: it permits wrong acceptance and in-sandbox unauthorized edits and records them for grading. `run.py` executes actions against actual disposable files, serializes evidence, reloads it, and invokes the separate grader. Temporary fixture directories are removed on exit.

Submission, delivery, acknowledgment, return persistence and acceptance are separate events. Logical ticks establish order. The seed randomizes concurrent return order; this is deterministic interleaving, not OS concurrency. A restart changes session identity and drops simulated volatile lead memory; recovery reads persisted records and transport observations. It does not emulate process termination or a model's lost context. Scripts explicitly choose recovery actions. Reports preserve failures and attempted actions; per-scenario execution errors are recorded and cause suite failure. Worker interruption changes simulated lifecycle and acknowledges it; subsequent worker steps test whether writes stop. External filesystem traversal/symlink escapes are prevented; unauthorized *simulated* actions inside fixtures are allowed and graded.

All 16 proposal scenarios have good/bad validation scripts, including six documented protocol gaps. The baseline isolates each failure; it does not represent arbitrary valid strategies or an exhaustive fault matrix. Judgment scenarios inspect preserved artifacts and source reads, not exact explanation labels. They remain synthetic harness plumbing tests, not proof of judgment or actual product behavior. `check` events alone are not execution evidence; supplied check artifacts are synthetic observations. No repository build, network service, model, or live Herdr is exercised. Session mapping, pane input and true crash/relaunch integration remain later work.

Run regression tests:

```sh
python3 -m unittest discover -s /path/to/evals/sim -p 'test_*.py' -v
```

Tests cover all-case discrimination, deterministic replay, seed variation, confinement with disposable external symlink targets, permissive environment vs independent grading, and artifact/order tampering. For future model integration, supply actions through Environment and preserve evidence; never expose the hidden invariants or scripted answers to the model. The current scripts are visible test doubles, not release evidence of v0.5 model performance.

## Task 8 hardening

Acceptance state invariants also require exact observed accepted_result history and reject direct set of accepted, including resets that try to hide rejected acceptance. Explicit acceptance events are required in the two successful acceptance scenarios. Other state choices remain permitted; scenario observation/artifact requirements supply their evidence. Deadline priority is explicitly graded. Authority and no-op retro require actual read/inspection results rather than preserved files alone. These are scripted evidence checks, not proof of model reasoning.
