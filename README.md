# team-lead

> **Outdated (v0.5.0, 2026-09-30).** The maintained team-lead now ships inside a larger agentic-engineering factory package, to be published later. This repository is not updated in the meantime.

[![skills.sh](https://skills.sh/b/romiluz13/team-lead-skill)](https://skills.sh/romiluz13/team-lead-skill)

Turn your coding agent into a real team lead for the agents you already have.

Most agents either work solo or hallucinate a team: fake teammates, fake progress, confident summaries of work nobody did. **team-lead** is an agent skill that makes your lead agent genuinely lead — onboard the actual people and agents on your project, delegate to them through the channels that really exist, verify their evidence, and keep the whole thing running across sessions.

It adds leadership. It does not install a mandatory process, pretend to have coworkers, or require any specific tool.

## What's new in 0.5

- **Record before dispatch.** A task exists in the team record before its prompt is sent, so a crash between the two can't orphan or duplicate work.
- **Corrections carry attempt ids.** A correction to task 7 is task 7.2 — a late `DONE 7` can't close it.
- **The file is authoritative; the ring is a hint.** Returns are persisted to disk; doorbells ring at most once and skip on a bounded wait, so a foreground-waiting lead never deadlocks the team.
- **One record root for parallel agents.** Milestone acceptance runs on the combined revision, with one named integration owner.
- **Fact-type reconciliation on resume.** Human intent, repo artifacts, coordination state, and unaccepted work each have an explicit winner instead of a blanket "trust the repo."
- **Evidence-backed no-op retros.** Zero changes is legitimate when the current practice is evidence-backed; a retro that must always change something accumulates instruction debt.
- **A scripted regression suite.** `evals/sim/` runs 16 team-lead scenarios with good/bad action pairs in one command, deterministic per seed — the same suite that gated this release.

## Install

```bash
npx skills add romiluz13/team-lead-skill
```

Install globally instead of per-project:

```bash
npx skills add romiluz13/team-lead-skill -g
```

Install to specific agents only:

```bash
npx skills add romiluz13/team-lead-skill -a claude-code -a codex -a cursor
```

Works with [73+ agents](https://github.com/vercel-labs/skills#supported-agents) — Claude Code, Codex, Cursor, Droid, OpenCode, Gemini CLI, Copilot, and more.

### Try it without installing

```bash
npx skills use romiluz13/team-lead-skill --skill team-lead --agent claude-code
```

## What the lead actually does

**1. Onboards the project and the team.** Learns the mission, roster, working agreement, and current state — from you, the workspace, and real team channels. Reuses an established team instead of inventing one. Never makes you repeat facts it can find.

**2. Maintains the project view.** Keeps a concise model of what's being built, who benefits, what's uncertain, and what could block delivery. Delegates separate views (architecture, user journeys, research) and connects their consequences.

**3. Leads the work autonomously.** Delegates documentation research and broad exploration so the lead can focus on decisions and integration. Assignments specify outcomes, context to read and save, ownership, acceptance evidence, and whether subagents are useful. Children share the team's resource limits; their parent checks and consolidates the results.

**4. Develops the team and itself.** Keeps a project-local development plan for each continuing member and the lead: demonstrated strengths, one improvement target, a real assignment to practice it, and a later check. Broader responsibility follows relevant evidence. Workers can challenge the lead's brief, and the lead checks whether its own changes reduced rework or improved the outcome.

**5. Verifies, hands off, and closes.** Defines completion evidence for the actual mission, reconciles what was checked versus what remains unexecuted, and closes the team visibly — thanking specific contributions and leaving one clear next step.

## How a session looks

```text
You:      Use team-lead. The mission is X. My agents are in these panes/channels.
Lead:     (onboards: mission, roster, working agreement, reads current artifacts)
Lead:     River — here's the failing import boundary. Outcome, pointers, allowed
          changes, acceptance evidence. Return when done or blocked.
River:    Found it: two downstream callers assume a public export. Reproducer attached.
Lead:     (inspects evidence, accepts, releases the dependent task)
Lead:     Next highest leverage is the contract mismatch. Quincy — research only,
          no writes; return the observation that would settle it.
```

The lead keeps a small `.team/state.md` (roster, active work, decisions, next actions) so a returning session can continue without restarting. Workers save evidence, decisions, uncertainties, and next steps at assigned locations; the lead maintains the accepted project view. Reuse existing project records and add files only when they help. See [team memory](team-lead/references/team-memory.md).

Each project has its own team history, member development plans, and lead learning. Matching agent names or model labels do not carry reputation between projects. The reusable skill shares the method; project records stay separate.

A [development plan](team-lead/references/development.md) changes the next assignment and checks the result. This improves context, task fit, and working instructions; it does not train model weights or establish general capability from a single success.

## Design principles

- **Never simulate a team.** No reachable teammates means establish the connection or do useful local work — never invent participation. An idle pane proves neither acceptance nor an unchanged artifact.
- **Evidence over reports.** Reports and memory are pointers to evidence, not substitutes. Consensus, rank, and repeated confident summaries do not establish correctness. A teammate can disprove the lead.
- **Authority is explicit.** Creating sessions, changing models, or installing infrastructure needs your authorization. Team leadership alone doesn't grant it.
- **Dispatch by reference.** Assignments carry outcome, context pointers, ownership, and acceptance evidence — scaled to ambiguity. Small tasks get small messages.
- **Coaching, not rankings.** Observations are tied to task conditions and revisited when conditions change. The lead's own mistakes stay in the same learning loop.
- **Transport-agnostic.** Works with terminal panes, subagent tools, inter-agent inboxes, or whatever surface your environment actually exposes. Herdr, tmux panes, Claude subagents — the method adapts; see [communication](team-lead/references/communication.md).

## What's inside

```text
team-lead/
  SKILL.md                     The leadership method (5 sections above)
  references/
    communication.md           Assignment/return contracts, delivery, interruption, recovery
    team-memory.md             Project boundaries, worker context, and handoff survival
    development.md             Practice, coaching, responsibility, and lead improvement
    herdr.md                   Leading agents in Herdr panes (channel, doorbell, waits)
    messages.md                Worked examples of strong vs. weak lead messages
  agents/
    openai.yaml                Interface metadata for OpenAI-compatible agents
evals/
  sim/                         Scripted 16-scenario regression suite (deterministic per seed)
```

## Requirements

- Any agent that supports the [Agent Skills spec](https://agentskills.io) (installed automatically by the command above).
- Teammates you can actually reach — terminal sessions, subagents, or an inter-agent channel. The skill works with one lead and whatever roster you provide; it adapts to the team's models, tools, and methodology (DDD, plain agile, or your own rules).

## License

[MIT](LICENSE)
