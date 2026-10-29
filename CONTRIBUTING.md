# Contributing

We welcome original curriculum improvements, accessibility, translations, tests,
and verified platform adaptations. Use synthetic examples; never publish student
or customer information. Contributions are offered under MIT and must be yours
to license. The current public edition and all generated output are in English.

To change a week, edit curriculum/plan.json and regenerate with
`python3 scripts/render_curriculum.py`. The four annual guides and first 40
lessons are generated from that file. For structural changes, edit the renderer too.

Before submitting:

1. Keep the after-school purpose and an activity possible with no budget.
2. Include an objective, task, evidence, and criterion someone else can review.
3. Distinguish verified facts, self-reports, inferences, and simulations.
4. For provider changes, cite official documentation, date, and actual testing.
5. Run `python3 -m unittest discover -s tests -v`, regenerate kits, and run
   `python3 scripts/ofs.py check`.

We do not accept earnings promises, invented mentors, copies of private
curriculum, unauthorized media, or recurring tasks enabled by default.
Marketing changes must not obscure zero tuition or the maximum refund.

Use issues for material errors and proposals, never private data. Follow
SECURITY.md for security concerns. This edition promises no response time,
personal mentoring, or professional support.
