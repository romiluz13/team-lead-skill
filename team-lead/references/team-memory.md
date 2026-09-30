# The team record

Read when establishing the project folder, at every cycle boundary, and on
resume. The record exists so a returning lead can make a sound next decision
without reading a conversation. It is a maintained working model, not a
transcript.

## Adopt what exists, start small

Use the project's existing records if it has any (`.team/`, `.orchestrator/`,
a plans folder — whatever is there). Only create a folder when none exists;
`.team/` is a suggestion, not a requirement. Start with one `state.md`; add
files when separation saves rereading or prevents write conflicts. These are
roles for information, not a mandatory schema. Link existing plan, decision,
test, and issue systems instead of building a second tracker.

```text
.team/
  state.md             mission, roster, active work, progress log, first resume action
  agreement.md         how this team works: channel, latitude words, this project's
                       brief additions and return deviations, definition of done,
                       reserved vs authorized — versioned by retros, with scars
  decisions.md         decision · why · evidence · who challenged it · what would reopen it
  lessons.md           "When <trigger>, do <rule>" + the scar it came from
  people/<member>.md   capacity ledger + strengths + one development target
  people/lead.md       the lead's own development, fed by retro answers
  tasks/<id>.md        the brief + the worker's return
```

Use workspace-relative paths; resolve absolute ones in the receiving
environment.

## One project, one record

Bind the folder to one project. The same member name in another project
starts with unknown capability here. Don't search, import, or merge
cross-project profiles; the skill supplies the method, not a shared dataset.
Moving records between projects takes an explicit user request.

## state.md

Keep it scannable:

- Mission and the finish condition (stated so it can pass or fail).
- The authority boundary — reserved for the human vs pre-authorized — as
  recorded in `agreement.md`.
- Roster: member, pane, agent kind, session id, role, current ownership.
- Active work: outcome, owner, latitude, expected time, return path.
- Progress log: append-only one-liners with evidence, pruned at milestones.
  This is what the human reads; keep it current and honest.
- The single first action on resume.

The lead owns the shared summary. Workers own their task notes and may
propose changes; coordinate writes so nobody overwrites current state.

## agreement.md, decisions.md, lessons.md

`agreement.md` is standard work: the channel and doorbell format, the
latitude words, this project's additions to the brief and return contract
(the full templates live in [communication](communication.md)), the
definition of done, and what's reserved for the human versus authorized
without asking. Retros edit it — a change to how the team works is a diff
here, not a sentiment. When a change comes from a failure, add a one-line
scar comment saying what happened.

`decisions.md` holds the accepted decisions with their why, evidence, who
challenged them, and the fact that would reopen them. A decision with no
reopen condition looks more certain than it is.

`lessons.md` holds rules that change future work: "When <trigger>, do
<rule>", plus the incident it came from. Record only lessons that change
work; merge near-duplicates and retire dead ones at milestones. Workers
propose lessons in their returns (`Lesson proposed:`); the lead checks one
against the evidence before it becomes a team rule. A short-lived worker
gets a task return, not a career file.

## The task file

`tasks/<id>.md` carries the brief and, below it, the worker's return in the
shape the return contract in [communication](communication.md) defines:
claims with status and the revision checked, what the brief should have said,
any proposed lesson. One file per task; the detail lives here, not in
messages.

## The distillation ritual (every cycle boundary)

Before the next dispatch:

1. **Always:** update `state.md` — 1–3 lines: what returned, what changed,
   what's next.
2. **If a return proposed a lesson or a correction happened:** `lessons.md`.
3. **If recognition or correction happened:** `people/<member>.md`, same
   moment, not later.
4. **If a retro or incident changed how the team works:** `agreement.md`,
   with the scar comment.

Later comes after compaction. A heavy ritual gets faked; a three-line habit
doesn't. At milestones, also replace stale status, resolve or reassign open
items, merge duplicates, and prune the progress log. When a stored claim
conflicts with new evidence, compare artifact identity and conditions before
deciding which is stale; write the supported conclusion with its evidence,
and tell affected owners rather than leaving the correction in an appendix.

## Resume reconciliation

After a session break or compaction:

1. Read `state.md`, then the repo: `git log` since the recorded commit.
2. List the team on its channel (Herdr: `agent list`, your workspace only);
   compare session ids. A new session id in a known pane is a new mind — it
   gets a re-brief from the record, not an assumption of memory.
3. On any conflict between the record and the repo, **trust the repo**, fix
   the record, and say what you fixed. Re-dispatching completed work is the
   most expensive resume failure; inspect the actual state before assigning
   anything.
4. Label unverified historical claims; don't redo stable completed work just
   because the session was new.
5. Take the single first resume action.

## What the record is not

Not a transcript: store conclusions and rationale, not streams of
deliberation. Not feelings: agent development here means better context,
instructions, task fit, and tools — a file does not update weights or
establish enduring capability. Not cross-project intelligence. Keep secrets
and confidential business context out of it entirely. Local notes never
imply permission to publish, move records across projects, or write to an
agent's separate global memory; publication takes an explicit scope and
content review. This skill never publishes team records automatically.
