# Local tool (optional)

Requires Python 3.10+ and the standard library. Commands use no network, models, API, database, or background tasks. Run from the repository root. Without Python, use the Markdown files and templates manually.

```sh
python3 scripts/ofs.py init --alias learner
python3 scripts/ofs.py lesson --year 1 --week 1
python3 scripts/ofs.py complete --alias learner --year 1 --week 1
python3 scripts/ofs.py profit private/learner/ledger.csv
python3 scripts/ofs.py profit examples/ledger-demo.csv --simulation
python3 scripts/ofs.py profit examples/ledger-demo.csv --simulation --share 0.5
python3 scripts/ofs.py pack
python3 scripts/ofs.py check
```

`init` creates a new private folder and refuses to overwrite one. `complete` records **self-reported** progress without assigning a grade or certifying sales. Repeating the same week does not duplicate it. The student/coach selects the next lesson based on review; the command does not advance automatically.

`profit` validates unique IDs, categories, dates, currency, and conversion. Use positive amounts; categories determine deductions. By default it calculates only `real` rows. `--simulation` calculates only simulations, never a mix. `--share` multiplies the indicator by the declared participation share (greater than 0 and at most 1), which must be supported outside the tool. It does not prove legal ownership.

Edit the CSV with a text editor or your own tool. If a spreadsheet changes dates, separators, or numbers, retain the exact header and decimal points before calculating. Validation errors stop calculation; invalid rows are not silently skipped.

`pack` writes five ZIPs and SHA256SUMS in release/. It uses an explicit content list and excludes private/, credentials, videos, and complete source materials. `check` validates structure, local links, and existing package hashes. It does not check remote link access or LLM behavior.

After editing curriculum/plan.json, regenerate guides with `python3 scripts/render_curriculum.py`, run tests, and package. Editing only a generated file will not preserve the change on the next build.
