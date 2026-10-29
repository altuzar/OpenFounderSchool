# OpenFounderSchool

**Your founder school after school. Open, free, and powered by your own AI agent.**

Build something useful, talk to customers, learn to sell, and keep honest books. For families, students, and after-school clubs. All curriculum, guides, prompts, and tools are in English.

> **“Graduate with US$1M in profit or get your tuition back. Tuition is US$0.”**
>
> This is our tuition promise with a sense of humor: the maximum refund is **US$0**. US$1M in cumulative profit is an extraordinarily ambitious goal, **not an assured outcome or an estimated probability of success**. Tools, materials, and business expenses may cost money and are not reimbursed. Read [the full explanation](docs/GUARANTEE.md).

## Start today

1. Read [START HERE](START-HERE.md) with a parent or responsible adult.
2. Choose [Grok Bot](adapters/grok-bot.md), [Claude Project](adapters/claude-project.md), [ChatGPT Work](adapters/chatgpt-work.md), [Pi](adapters/pi.md), or [Hermes](adapters/hermes.md).
3. Use the [coach instructions](prompts/COACH.md) and [curriculum](curriculum/OVERVIEW.md). The [release](release/README.md) kits collect everything for upload without coding.
4. Say: **“Start OpenFounderSchool. Ask onboarding questions one at a time. Begin year 1, week 1 in simulation mode with a zero-dollar budget.”**

For agents with file access, open this repository as the working folder. Read [AGENTS.md](AGENTS.md); the platform guides explain what loads automatically and what you need to attach.

## What's included

| Material | Purpose |
| --- | --- |
| [Four-year path](curriculum/OVERVIEW.md) | 160 weeks, 6 hours a week; 960 hours total |
| [Year 1](curriculum/years/year-1.md) | 40 lessons with exercises, evidence, questions, and completion criteria |
| [Years 2–4](curriculum/years/year-2.md) | Weekly plans for operating, growing, and preparing a handoff |
| [Parent handbook](docs/PARENTS.md) / [student handbook](docs/STUDENTS.md) | Organization, permissions, and habits |
| [Mentors](mentors/README.md) | Eight AI coaching roles and a human mentor protocol |
| [Templates](templates/README.md) | Interviews, offers, experiments, numbers, decisions, and pitches |
| [Research](research/README.md) | Sources, YouTube inventory, notes, and coverage limitations |
| [Local tool](docs/CLI.md) | Create a private student folder, look up lessons, and calculate a profit indicator |
| [From exercise to business](docs/VENTURE-PLAYBOOK.md) | Selection, tests, pricing, capacity, and evidence-based growth |

## Designed for after school

Three 90-minute sessions and one 90-minute review: **6 hours a week**, 40 weeks a year. Fit the calendar around school, rest, and other activities. Move more slowly if needed. Suggested path for ages 14–18; younger students work through an adult with adapted activities. Before using any provider, the adult checks its current age requirements, authorized access, and terms. This repository does not grant access to third-party services.

This does not replace an accredited school or issue official diplomas. You can complete it with paper, local files, and simulations. Real sales are optional and require suitable organization and supervision. Assessment recognizes evidence and skills even when the business makes no sales.

## Cost and independence

- Original curriculum and code: **MIT**. Copy, modify, and redistribute them, including commercially, while retaining the license.
- No backend, central account, telemetry, cron, required newsletter, or project subscriptions. At rest: **0 AI calls and 0 database writes**.
- AI, hosting, and payment providers have their own terms and pricing. You do not need all five: choose one or work offline. See [budgeting](docs/COSTS.md).
- Independent project inspired by public [Founders School](https://founders.school/) materials. No affiliation with Founders School, Alpha School, or their mentors. This repository does not redistribute their private curriculum, books, videos, or complete transcripts. See [attribution](NOTICE.md).

## For contributors

Python 3.10+; no external dependencies or network calls during normal use.

```sh
python3 scripts/ofs.py check
python3 -m unittest discover -s tests -v
python3 scripts/ofs.py pack
```

Read [CONTRIBUTING](CONTRIBUTING.md), [security](SECURITY.md), [validation limits](docs/VALIDATION.md), and the [quickstart](README.en.md).
