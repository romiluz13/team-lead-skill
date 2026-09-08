# Working with the available team channels

Read when onboarding teammates, choosing a communication surface, dispatching
ambiguous work, or recovering from missing replies. Use real capabilities exposed
by the current environment. The core leadership method does not depend on this
file's Herdr example or on any particular agent provider.

## Discover before dispatch

Identify the user-provided agents and available channel: terminal sessions,
subagent tools, an inter-agent inbox, or another explicitly authorized surface.
Confirm target identity, current activity, workspace and access. Existing busy
work belongs to its current owner; coordinate a handoff before replacing it.

A friendly model name is a label unless the environment exposes verified model
identity. Record that distinction. Do not change a session's provider or create
replacement agents merely because a preferred model is absent. Ask for a missing
connection when required, while continuing work that does not depend on it.

Adapt to the transport:

- With a shared filesystem, send a task/plan path plus the smallest necessary
  instruction. Confirm the recipient can reach the referenced artifact.
- Without shared storage, transmit the relevant excerpt or attach the artifact,
  including its identity and limits. Do not send a path the recipient cannot read.
- With no messaging capability, clearly state what cannot be delegated. Prepare
  a concise handoff or work locally as authorized; never invent replies.

## Assignment and return contract

Give each assignment enough context to make independent judgment possible:

> Outcome and reason; source/task pointers or self-contained context; current
> artifact/revision; ownership and allowed changes; dependencies and constraints;
> acceptance evidence; when and how to return.

Include methodology instructions only when applicable, preferably by reference to
the existing source. Ask for alternatives or objections when the approach is
uncertain. State whether a task is research, implementation, review, or a bounded
experiment so a reviewer does not quietly become a second writer.

A useful return distinguishes:

> Finding or change; evidence actually inspected or produced; artifact identity;
> checks run and results; limitations, failed attempts and cleanup; decision or
> next action needed.

Review can use an uncommitted or non-Git artifact. Identify the delivered snapshot
with an accessible copy, attachment, or patch and its base; use a digest when
needed to distinguish versions. Committing solely to obtain a review is optional.

Short, clear messages are sufficient for routine work. Avoid requiring a report,
manifest, meeting, or extra reviewer for every exchange. The lead consolidates
results and informs dependent owners when a decision changes.

## Delivery, interruption, and recovery

Sending a message, receiving an acknowledgment, completing work, and accepting its
result are distinct events. Use task identity and observed state to avoid treating
an old completion notice as the answer to a new assignment.

On timeout, inspect the target before resending; delivery may already have
succeeded. Bound waiting to the urgency and expected task duration. Keep the
human informed of consequential changes without narrating routine polling.

If a worker becomes unavailable, preserve its evidence and inspect active work
before reallocating ownership. Stop or isolate any previous writer before another
can modify the same artifact. An unavailable service is not evidence of poor
reasoning. After a restart, refresh the contact/session mapping and handoff.

A stop or scope change must reach affected workers. Check for active mutations
and owned temporary resources before assuming the team stopped. A reflection or
thank-you message is not an instruction to resume old tasks; say so when context
could be ambiguous.

On a stop request, promptly notify every active owner, prevent new assignments,
and preserve existing uncommitted work. Report each owner's observed status;
an unacknowledged stop is still unconfirmed, not a stopped team. If the channel
cannot reveal delivery, record that uncertainty and use a bounded attempt to
communicate the stop rather than resending the old work. Preserve by default;
discarding, committing, or transferring work follows the existing authority.
Do not delay a requested summary indefinitely for unreachable workers, or make
the human choose whether to abandon work merely to end the session.

## Herdr example: only when selected and available

Use Herdr when the user selects it or explicitly asks to work with its agents.
Read the available `herdr` skill if present and inspect installed CLI help before
control operations. Verify the environment requirement described by that skill.
Discover the real workspace, pane and agent identifiers; never bake previous
session IDs or machine paths into this methodology.

The user may create and name all panes. Onboard that roster in place. Respect
focus and existing work. Read results through the agent/pane surface and use
shared task paths where accessible. An idle pane proves neither acceptance nor
an unchanged artifact; inspect the returned evidence for the assigned task.

Other transports should supply the same identity, dispatch, observation and
handoff functions through their own documented tools. A missing optional Herdr
skill does not disable leadership through another available, authorized channel.
