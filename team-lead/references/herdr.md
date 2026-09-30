# Leading a team through Herdr

Read when the team's channel is Herdr: the agreement says so, or the roster
lives in Herdr panes. This file covers how to lead through Herdr. For command
syntax, load the `herdr` skill and trust the installed CLI's help over this
page. The user choosing Herdr for this team counts as the explicit mention
that skill requires.

First, check you're inside Herdr: `test "${HERDR_ENV:-}" = 1`. If you're not,
say so and lead through whatever other channel is authorized. Don't drive a
Herdr session from outside it.

## Know who's on the team

`herdr agent list` returns every agent on the server, including other
people's teams in other workspaces. Filter to `workspace_id` equal to
`$HERDR_WORKSPACE_ID`, or to the workspaces the agreement names. Anything
outside that set isn't yours to onboard or message.

For each teammate, record in `state.md`: the name, `pane_id`, `agent` kind,
and `agent_session.value` when present. The kind is Herdr's detection, which
is more reliable than a model name someone typed in a message, but it still
isn't a model version.

Names are what the team runs on: briefs, the doorbell, and the record all
address teammates by name. If panes the user set up for this team have no
name, give them short, stable ones with `herdr agent rename <pane> <name>`,
and note it in `agreement.md`. Name your own pane too, so workers can reach
you.

A new `agent_session` value in a known pane means a new session with none of
the old context. Re-brief it from the record. Don't assume it remembers
anything.

## The attention loop

1. **Look:** the filtered `agent list` plus `state.md`.
2. **Pick** the highest-value moment. Rough order: a `blocked` teammate, a
   report waiting for you, an idle teammate with valuable work, a teammate
   quiet past its expected time, then a reflection that's due.
3. **Act** on that moment.
4. **Record** in `state.md`; a task line goes in before its prompt is sent.
5. **Wait** with a limit. Either the doorbell wakes you, or you use
   `herdr agent wait <name> --timeout <ms>`. Pick the timeout from how long
   the task should take. Don't run a bare polling loop. If your harness can
   run commands in the background, run the wait there so finishing it wakes
   you.

## Dispatch

- Put the brief in `<record>/tasks/<id>.md`, where `<record>` is the
  record root's absolute path
  ([communication](communication.md#parallel-agents-in-one-repository)), and
  send a short prompt that points to it: `herdr agent prompt <name> "Task
  <id>: read <record>/tasks/<id>.md and start. Ring me when done."` Tiny
  tasks can go inline. A correction uses its attempt id (`Task 7.2`).
- Prompt only a teammate that is `idle` or `done`. Text sent to a `working`
  agent may interleave, queue, or behave differently depending on the
  receiving harness; verify per harness. If you need to stop work, use the
  stop procedure below. Don't send a message instead.
- When dispatching to several teammates, send all the prompts without
  `--wait`, then wait on each. `--wait` on the first one leaves the others
  unassigned.
- A successful prompt only proves the text was submitted, not that work
  started. If a prompt times out or stalls, run `agent get` and `agent read`
  before sending anything again. The first one may already have landed.

## The doorbell

The return happens in two parts:

1. The worker writes its full report to the file named in the brief.
2. The worker waits up to about a minute for your pane to be free
   (`herdr agent wait <lead> --until idle --until done --timeout 60000`),
   then sends one line: `herdr agent prompt <lead> "DONE <id> <path>"`. Use
   `BLOCKED <id> <path>` or `QUESTION <id> <path>` in the same way. On
   timeout it skips the ring; the file is enough.

Put both steps and your pane's name in every brief that expects a return.
Tell workers to ring at most once. The file is authoritative; the ring is
only a hint. This keeps report detail out of both transcripts, and it
survives your own compaction because the file is still on disk. A
foreground `agent wait` on a worker shows you as `working`, so its ring
gets skipped: run your wait in the background where the harness allows,
otherwise keep it short and check the expected return files on each wake.

## Reading a pane

The return file is your first source of evidence. A pane transcript is the
last. When you need the pane (a teammate has gone quiet, a UI is blocked, or
a doorbell never came), read a small window:
`herdr agent read <name> --source recent-unwrapped --lines 40`. Widen it only
if that doesn't answer the question. Every line you read comes out of the
context you need for judgment.

`idle` or `done` doesn't mean the work was accepted, or that the artifact
hasn't changed. Accept work only after checking its evidence.

## Blocked

`blocked` means Herdr sees an approval or question UI. Check it with
`agent get` and a short `agent read`.

- **Approval to run a command, edit, or access something:** this is
  reserved for the human unless `agreement.md` pre-authorizes that exact
  class of action. Send the human the command, the pane, whether it's in
  scope, whether it can be reversed, and your recommendation. Leave that pane
  held and keep the rest of the team working.
- **A question about the task:** answer it if the answer is within your
  authority. Otherwise treat it as a question for the human.

Never approve a dialog just to keep things moving.

## Quiet teammates

A teammate that's still `working` past the time you expected, or is in
`unknown`, isn't evidence of anything yet. Read a small window, then work out
which it is:

- **Progressing slowly:** extend the wait once, with a new limit.
- **Thrashing** (repeating attempts that fail): stop it and re-brief with
  what's missing.
- **Lost the thread** (re-asking settled questions, contradicting its own
  earlier findings, ignoring constraints in the brief): stop it and re-brief
  from the record. With authority, start a fresh session.
- **A service or tool failure:** that's a problem with the environment, not
  with the teammate's reasoning. Record it that way.

Take one bounded action and record it.

## Stopping and scope changes

To interrupt, use the kind's interrupt, usually
`herdr agent send-keys <name> esc` (see the herdr skill for other kinds).
Wait for `idle`, then send a plain message saying what stopped, what to keep,
and what happens next. A stop that hasn't been acknowledged is unconfirmed.
Record it that way. A thank-you or a reflection message is not an instruction
to resume old work. Say so if the teammate could read it that way.

## Paging the human

`herdr notification show "<title>" --body "<one line>" --sound request` is
only for things the human needs to act on: an approval, a product decision,
or bad news. It's a pager, not a feed. Routine progress goes in the progress
log in `state.md`.

## Keeping or restarting a teammate's session

Keep the same session for related follow-on work. Its context and the
feedback you've already given it are an asset. Start a fresh session, with
authority, for unrelated work or once a teammate has lost the thread. The
development record belongs to the member, not the session, so carry it into
the next brief.

## House rules inherited from the herdr skill

Use `--no-focus`, and leave the user's focus where it is. Don't close panes,
tabs, or workspaces you didn't create. Parse IDs from JSON rather than
predicting them. Never stop the Herdr server.
