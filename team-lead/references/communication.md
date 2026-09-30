# Briefs, returns, and team channels

Read when onboarding teammates on a channel, writing a brief for ambiguous
or consequential work, dispatching review or research, running agents in
parallel, or recovering from a missing reply or a stop. The method doesn't
depend on any provider or transport. When the channel is Herdr, also read
[herdr](herdr.md).

## Discover before dispatch

Find the real channel: terminal panes, subagent tools, an inbox, or another
authorized surface. Confirm each target's identity, current activity,
workspace, and access. Work already in progress belongs to its owner;
coordinate a handoff before replacing it.

A friendly model name is a label unless the environment verifies it. Record
the difference. Don't switch a session's provider or create replacements
because a preferred model is missing. Ask for a missing connection, and keep
doing the work that doesn't need it.

Adapt to the transport:

- **Shared filesystem:** send a path plus the smallest instruction, and
  confirm the recipient can read it.
- **No shared storage:** send the excerpt or attachment with its identity and
  limits. Never send a path the recipient can't open.
- **No messaging:** say plainly what can't be delegated, then write a handoff
  or work locally as authorized. Never invent replies.

## The brief

Give enough context for independent judgment, and no more. Small tasks get
small briefs.

- **Why:** one sentence tying the task to the user's outcome. It's the
  tiebreaker for every call you didn't anticipate.
- **Outcome**, not procedure. Leave the approach open where judgment matters.
- **Kind:** research, implementation, review, or a bounded experiment, so a
  reviewer doesn't quietly become a second writer.
- **Latitude:** *Look* (investigate, change nothing) · *Propose* (recommend,
  the lead decides) · *Do & tell* (decide within these bounds, report) ·
  *Own* (end to end, report at milestones).
- **Pointers**, worded by reach condition: "read the deploy section of
  `ops.md` before planning" beats "see `ops.md`". The wording decides whether
  the worker reaches the material. Cite method instructions by reference.
- **Current state:** the artifact or revision to start from; ownership and
  allowed changes; dependencies and constraints; shared resource limits.
- **Least sure of:** the assumption most likely wrong, and a request for the
  one observation that would settle it. This replaces "any concerns?", which
  gets silence or invented objections.
- **Done means:** named claims, each with its check (below).
- **Stop rule:** after a bounded number of failed approaches or a time cap,
  stop and write up what was learned. Stopping honestly is a good outcome;
  reinterpreting the goal to look successful isn't.
- **Development target**, when this task can exercise it, with any earlier
  feedback that applies.
- **Subagents:** none, named, or the worker's call within an envelope (below).
- **Return:** the file to write and how to signal (on Herdr, the doorbell).

State the target behavior positively. A prohibition pulls the forbidden
behavior into the worker's context, so keep one only as a hard guardrail,
paired with the positive target.

## Acceptance evidence

Name the claims the worker must establish and the check for each. On return,
each claim gets a status: **passed**, **failed**, or **untested** with the
reason. A claim the return doesn't address is untested, never assumed.
Anchor each status to the revision, artifact identity, or digest it was
checked against, so a later change can't make old evidence look current.
For a defect fix, capture the failing state while reproducing, before the
fix, when it's cheapest.

## The return

One spec; the task file (`tasks/<id>.md` in the team record) holds it below
the brief.

- **Result:** the finding or change, and the artifact identity (commit,
  path, digest).
- **Claims:** each with its status and the revision checked.
- **Evidence:** what was actually inspected or produced, as pointers.
- **Limits:** failed approaches, what's unknown, cleanup done or owed.
- **Decision needed**, if any, with a recommendation.
- **What I wish the brief had said:** one line, or "nothing".
- **Lesson proposed:** optional; "When <trigger>, do <rule>". The lead checks
  it before it enters the shared record.

Keep the signal message compact: status, task id, and the path. The detail
lives in the file. The file is authoritative and the signal only a hint:
write the file first, send the signal at most once, and skip it if the lead
isn't ready within a bounded wait. The lead's own wait checks the expected
return files, not only the channel.

A review can target uncommitted or non-Git work. Identify the snapshot with
an accessible copy or patch and its base, plus a digest when versions could
be confused. Committing only to get a review is optional.

**Research returns** add: the answer, primary sources with version and scope,
contradicting evidence, and what's still unknown. The lead synthesizes and
checks the decisive source rather than repeating the search.

## Review and disagreement

Give reviewers the requirement and the raw artifacts before your favored
explanation. The hard lines in SKILL.md apply: no suppressed findings, no
wrong finding accepted for a clean score, and a named cycle cap.

When reviewers disagree, compare their rationales and the decisive evidence.
A factual dispute is settled by checking the artifact. Reframe the question
for everyone only when the disagreement exposes competing readings of the
requirement. Averaging verdicts or siding by rank settles nothing.

A review score is a gate, not a verdict. Resolve each finding by fixing it
or rebutting it with stated grounds; user requirements and accepted project
decisions outrank a reviewer's preference. At the cap with findings open,
stop and report.

## Subagents and recursion

For each assignment choose: the worker does it directly, uses named
subagents, or decides within an envelope. Children fit independent
questions, useful context isolation, or independent review. A small lookup or
a tightly coupled edit stays with its owner. Spawning is not progress.

The envelope names the allowed child roles, slots, the shared budget (time,
iterations, or tokens where measurable), and the stop or escalation
condition. Descendants count against the same team limits; delegation
doesn't reset the allowance. If cost can't be measured, say so and bound
calls, time, or rounds. Verify the harness's real capacity and your authority
before spawning; otherwise use an existing worker or a serial plan. Change
models only with authority.

A parent gives children the same project boundary, pointers, ownership, and
evidence contract, and checks their returns. Before yielding, it reports
active descendants and remaining work. At a limit, it returns partial
findings and the missing evidence instead of adding another layer.

## Parallel agents in one repository

Isolation is mechanical, not social. Each agent gets its own worktree and a
branch from the default branch. Never build on the default branch, and never
reuse another agent's worktree, branch, or uncommitted work.

Before starting, enumerate every open pull request with pagination and check
its changed files. On GitHub:

```sh
gh api --paginate 'repos/{owner}/{repo}/pulls?state=open&per_page=100' --jq '.[].number'
gh pr diff <n> --name-only
```

If the task needs files another change is editing, stop and ask. If the
enumeration fails or was bounded, report incomplete coverage, not "no
overlap". Resolve lockfile conflicts by regenerating, never by hand-merging.

Worktrees don't isolate the machine. Confirm a dev-server port answers the
authorized agent's own process before trusting what it serves, and never run
schema experiments against a shared database. A green check served by
another agent's process is not this task's evidence.

The team record has one root, named by absolute path in `agreement.md`. Each
agent resolves record paths against that root, never against its own
worktree; a brief gives the absolute path when worktrees differ.

Name one integration owner for parallel work. Milestone acceptance runs on
the combined revision; branches that are each green alone don't prove the
merge is.

Routine exchanges need short messages, not a report, manifest, meeting, or
extra reviewer each time. The lead consolidates results and tells dependent
owners when a decision changes.

## Delivery, interruption, and recovery

Sending, acknowledgment, completion, and acceptance are four different
events. Use the task id and observed state so an old completion isn't read
as the answer to a new assignment; a correction carries an attempt id
(`7.2`) and keeps its own return section.

On a timeout, inspect the target before resending; the first send may have
landed. Bound each wait by urgency and expected duration. Tell the human
about consequential changes, not routine polling.

When a worker becomes unavailable, preserve its evidence and inspect its
active work before reassigning. Stop or isolate the previous writer before
anyone else touches the same artifact. An unavailable service says nothing
about reasoning quality. After a restart, refresh the contact and session
mapping and re-brief from the record.

A stop or scope change must reach every affected worker. Check for active
mutations and owned temporary resources before assuming the team stopped. A
thank-you or reflection message isn't an instruction to resume old work; say
so when it could be read that way.

On a stop request: notify every active owner, prevent new assignments, and
preserve uncommitted work. Report each owner's observed status. A stop nobody
acknowledged is unconfirmed, not done. If the channel can't show delivery,
record that and make one bounded attempt to communicate the stop, rather than
resending old work. Preserve by default; discarding, committing, or
transferring follows existing authority. Don't hold a requested summary
indefinitely for unreachable workers, and don't make the human choose to
abandon work just to end the session.

## Writing for people

Briefs, coaching, reports, and closing summaries are read by people and
agents alike; write them like it. Plain words: use, not utilize; help, not
facilitate. Active voice, with the actor named. Cut filler: "in order to"
becomes "to", "due to the fact that" becomes "because". One hedge is enough.
Say the mechanism or the number, not the feeling. Keep sentences short and
vary their length. A sentence that could appear unchanged in any project's
message says nothing about this one; cut it. Have an opinion when the
evidence supports one; a neutral list of pros and cons usually dodges the
judgment. No decorative emoji. Straight quotes. Apply these rules to text you
write or change; leave prose you didn't touch alone.

## Other channels

Herdr has its own guide: [herdr](herdr.md). Any other transport has to supply
the same functions through its own documented tools: identity, dispatch,
observation, and handoff. A missing optional channel skill doesn't stop you
leading through another authorized channel.
