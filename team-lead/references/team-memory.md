# The lead's working memory

Read when establishing the project folder, recording coaching, reflecting, or
resuming a team. The folder should let a returning lead make a sound next
decision without reading the entire conversation. It is a maintained working
model, not a transcript, personnel database, or collection of private thoughts.

## Start small and reuse what exists

Use the user's existing team/project records as the source of truth. Choose one
local folder only if none exists; `.team/` is a suggested name, not a requirement.
Begin with one `state.md`. Add files when separation reduces rereading or write
conflicts. A long-running project may grow into:

```text
.team/
  state.md             Current outcome, roster, ownership, next actions
  project.md           Durable project view and working agreement, if substantial
  people/<member>.md   Useful observations and next-assignment guidance
  tasks/<task>.md      Bounded task context and evidence, when a message is insufficient
```

For a small team, keep useful observations inline in `state.md`; separate member
files only when the history helps future assignments. These are roles for
information, not a mandatory directory schema. Keep existing plan, decision,
test, and issue systems; link them rather than building a second
workflow tracker. Use workspace-relative references where portable; when a tool
needs an absolute path, resolve it in the receiving environment.

## What must survive a handoff

Keep the current state easy to scan:

- Mission and completion boundary; current milestone and why it matters.
- User constraints, chosen method, reserved decisions, and authorized actions.
- Roster: member handle, contact/session reference, model label and its source,
  availability, assigned role, access limits, and current ownership.
- Active work: outcome, owner, dependencies, status, artifact/revision pointer,
  required evidence, outstanding reply or retry, and next action.
- Accepted decisions: decision, short rationale, evidence pointer, relevant
  alternatives, and what new fact would justify reconsidering it.
- Open risks, unresolved disagreements, and human questions; attach ownership or
  a specific unblock condition instead of leaving an unexplained warning.

Retain a small project view: user journeys or domain outcomes, important
architecture/operational boundaries, and the assumptions currently driving
priorities. Write a conclusion and its rationale, not a stream of deliberation.

The lead owns the shared summary. Teammates can own separate task notes or propose
updates; coordinate writes to avoid overwriting each other's current state.
Store raw logs or large artifacts separately only when they are useful evidence.
Preserve significant failures and their eventual disposition without copying the
same log or status into multiple files.

## Teammate observations and coaching

Create a member note when there is a useful observation to retain. A model name
alone is not a performance record. Track the actual member/session and the task
conditions; a replacement using the same display name is not automatically the
same teammate. Mark missing context as unknown instead of reconstructing a
convenient history for an inherited judgment.

Use this compact shape, adapting it to the evidence:

| Field | What belongs here |
| --- | --- |
| Context | Date, member/model identification, task, artifact, scope and relevant constraints |
| Observation | What the teammate did, discovered, delivered, or missed; link the supporting record |
| Interpretation | The lead's tentative judgment and alternative explanations |
| Next guidance | A concrete change to assignment, context, pairing, verification, or coaching |
| Revisit | Later evidence that confirmed, weakened, or replaced the interpretation |

Example, fictional and illustrative:

> River traced an import failure through two downstream callers and produced a
> minimal reproducer. The report also assumed a helper was public without checking
> exports. This suggests a useful fit for boundary investigations; next time ask
> for the exact export/caller chain before classifying public impact. One observed
> task supports this assignment choice, not a general model ranking.

Balance strengths and errors. Separate product defects, faulty research claims,
harness mistakes, instruction-following problems, and service outages. Do not
invent numerical error rates or compare raw counts across unequal work. Record
feedback delivered and whether the next similar task improved. Coaching changes
instructions and working conditions; it does not claim to retrain the model.

Apply the same scrutiny to the lead: missing context, shifting scope, excessive
review, poor task division, or premature acceptance may explain a worker's result.
Invite disagreement and corrections to the record. Retain candid feedback without
hostility, model stereotypes, or ceremonial performance grades.

## Refresh instead of accumulating

At a milestone or before handing over, replace stale status, resolve or reassign
open items, and merge duplicate observations. Preserve the reason behind important
changes; archive detail only when someone may need it. When a stored claim
conflicts with new evidence, compare artifact identity and conditions before
deciding which claim is stale. Update the current summary with
the supported conclusion, its evidence and the reason for correction; preserve the
old evidence under its actual boundary. Inform affected owners rather than
leaving the correction only in a later appendix.

On re-entry:

1. Read the current state and applicable project instructions.
2. Confirm the project/artifact revision and actual reachable teammates. Inspect
   active work before repeating assignments; a changed session requires a fresh
   identity and ownership check.
3. Check evidence likely to have changed or important to the next decision.
   Label unverified historical claims; do not redo stable completed work simply
   because the conversation was compacted.
4. Reconstruct the critical dependency, send the minimum useful context, and
   continue from the actual unfinished task.

Keep secrets and confidential business context out of reusable skill material.
Store only authorized, necessary project information in the local team folder.
Local notes do not imply permission to publish, move across projects, or write to
an agent's separate global memory system. Publication needs a deliberate scope
and content review; this skill never publishes team records automatically.
