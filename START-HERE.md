# Your first afternoon

Allow 45 minutes with an adult and 45 minutes for exploration. You need a notebook or local folder, not a credit card.

1. The student decides whether to participate and what interests them. The adult agrees on a sustainable schedule. Do not turn the financial goal into family pressure.
2. Choose a format: individual with an adult, team of 2–3, or club of 4–8. Identify a club lead and a private family communication channel. This repository does not administer a central community.
3. Record only an alias, age range, language, available hours, interests, and budget. Do not upload a home address, school, birth date, identity documents, or passwords.
4. Read [the working agreement](docs/SAFETY.md). Start in simulation mode. The AI prepares drafts; the student explains and executes the parts they understand.
5. Follow your platform adapter. If it does not support files, paste COACH.md and the current lesson. Do not paste the entire repository into every message.
6. Complete [the first lesson](curriculum/lessons/y1-w01.md). Save a list of everyday problems, one hypothesis, and a small plan for this week.
7. Finish with what you did, what the AI did, what you learned, and your next step.

## If you use a terminal

From the repository root:

```sh
python3 scripts/ofs.py init --alias learner
python3 scripts/ofs.py lesson --year 1 --week 1
```

This creates `private/learner/`, which Git ignores. An alias accepts only ASCII letters, numbers, hyphens, and underscores. Never use a student's full name as a public alias. Do not publish the private folder. A `.gitignore` rule does not remove files already published.

## Starting message

```text
Use OpenFounderSchool as an after-school curriculum. Read the coach instructions
and current lesson. Interview us one question at a time: respondent's role,
alias, age range, language, available time, and interests. Ask about a responsible
adult before external activities. Do not collect sensitive data. Do not ask me
to create accounts or connect email to get started. Budget US$0, simulation mode,
no external messages or scheduled tasks. Finish with one 20-minute action and a
summary to save in my private folder.
```

## Troubleshooting

- The AI forgets: load the latest `checkpoint.md`; do not rely on implicit memory.
- It cannot read a ZIP: unzip it and upload the Markdown files or the kit's `STARTER.md`.
- It has no tools: use conversation mode and copy the deliverables yourself.
- The provider does not allow the student's age: work on paper with an adult; do not falsify age or share credentials.
- The work becomes exhausting: reduce sessions to 45 minutes or pause. Record where to resume.
