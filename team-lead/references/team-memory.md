# The lead's working memory

Read when establishing the project folder, recording coaching, reflecting, or
resuming a team. The folder should let a returning lead make a sound next
decision without reading the entire conversation. It is a maintained working
model with development records, not a transcript or collection of private thoughts.

## Project boundary

Bind the folder to one project identity and workspace. Keep that project's lead
history, member profiles, development plans, decisions, and evidence there.
The same model or member name in another project starts with unknown capability
in this project. Do not search, import, merge, or maintain cross-project profiles.
A shared skill supplies the method, not a shared team dataset. Moving records
between projects requires a separate explicit user request.

## Start small and reuse what exists

Use the user's existing team/project records as the source of truth. Choose one
local folder only if none exists; `.team/` is a suggested name, not a requirement.
Begin with one `state.md`. Add files when separation reduces rereading or write
conflicts. A long-running project may grow into:

```text
.team/
  state.md             Current outcome, roster, ownership, next actions
  project.md           Durable project view and working agreement, if substantial
  people/<member>.md   Project-local capability evidence and development plan
  people/lead.md       Lead development and coordination improvements
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

## Worker context contract

At dispatch, give the worker the project boundary, relevant state/task/decision
pointers, applicable feedback, and exact write location. Explain what it owns and
what only the lead may accept into shared state. Send the smallest context that
supports sound judgment, not the whole team's history. If a worker cannot reach
a file, supply the relevant excerpt and its artifact identity.

The worker reads that context before acting. At a meaningful decision, blocker,
or handoff, it updates its task note with:

- Current result and artifact/revision; checks and their observed outcomes.
- Decisions and concise rationale, uncertainties, and what would change the answer.
- Failed approaches worth avoiding and the next concrete action.
- What worked, what needs adjustment, and whether the previous feedback helped.

Store useful conclusions, not private reasoning transcripts or invented feelings.
Record reflection as the worker's assessment until evidence supports it. A worker
proposes a general lesson; the lead checks it before changing the shared view or
member record. Use [development](development.md) for coaching and responsibility
changes. Keep task notes and accepted team state under separate ownership.

Before compaction or a session change, save work still held only in context.
On receipt, the lead reconciles accepted results, dependencies, and decisions;
notifies affected owners; and keeps one first action for resume. Keep necessary
raw evidence outside the short summary and link it rather than duplicating it.

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
