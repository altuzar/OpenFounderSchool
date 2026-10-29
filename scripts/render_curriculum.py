"""Render original curricular data into English guides (offline)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render():
    data = json.loads((ROOT / 'curriculum/plan.json').read_text(encoding='utf-8'))
    for year in range(1, 5):
        weeks = [e for e in data['entries'] if e['year'] == year]
        parts = [f'# Year {year} — weekly guide', '',
                 '40 active weeks × 6 hours = 240 hours. Adjust dates, breaks, and accessibility with your family.', '',
                 'Original OpenFounderSchool material. Simulations never count as real customers or profit.', '',
                 'Read [the overview](../OVERVIEW.md) and [the rubric](../../docs/ASSESSMENT.md).', '']
        for e in weeks:
            w = e['week']
            parts += [f'## Week {w}: {e["title"]}', '', e['concept'], '',
                      f'- **Build:** {e["build"]}', f'- **Test:** {e["test"]}',
                      f'- **Deliver:** {e["artifact"]}', f'- **Criterion:** {e["criterion"]}', '']
            if year == 1:
                parts += [f'[Open the full lesson](../lessons/y1-w{w:02d}.md).', '']
                reading = ['A','A','A','A','C','D','C','B','B','H',
                           'E','E','E','E','E','B','C','C','E','H',
                           'B','F','B','D','B','B','H','F','E','H',
                           'G','G','C','D','F','H','D','E','H','H'][w - 1]
                text = f'''# Year 1 · Week {w}: {e['title']}

**Total time: 6 hours**. Three 90-minute blocks and one 90-minute family review. Split blocks if needed. Initial budget US$0; simulation mode unless an adult authorizes specific activities.

## This week's idea

{e['concept']}

Read unit **{reading}** of the [original readings](../READINGS.md). Explain it using an example different from the text. Reading and discussion happen inside the first block, not as additional homework.

## Block 1: understand and make your first attempt

Spend 10 minutes checking energy and previous evidence; 20 reading and discussing; 20 on your first draft; 10 on a break; 25 practicing with coach support; and 5 recording what changed. Ask: what do I know from experience, and what am I assuming? The coach requests your attempt before proposing a complete solution.

## Block 2: build

{e['build']}

Use 10 minutes to set scope, 30 to work independently, 10 for a break, 30 to improve with help, and 10 to check the deliverable. If stuck, reduce the outcome to something you can explain in 20 minutes. Document what the AI did and what you understood yourself.

## Block 3: test and record

{e['test']}

Allow 15 minutes for test preparation and permissions, 30 for testing, 10 for a break, 25 for analysis, and 10 for recording evidence. If external action lacks permission, use roleplay labeled SIMULATION. Keep a result that contradicts your idea, or honestly explain that you have not found one yet. Do not invent evidence to fill a table.

## Block 4: review with an adult or mentor

Show **{e['artifact'].rstrip('.')}**. Use the [rubric](../../docs/ASSESSMENT.md): problem, construction, communication, numbers, and judgment. The adult listens to your explanation and asks:

1. What did you observe, and what are you assuming?
2. How could someone else verify your main claim?
3. What would you change with half the time or a zero-dollar budget?

**This week's criterion:** {e['criterion']}

If evidence is missing, agree on a smaller practice before taking further external action. A sale is not required. Complete the [weekly review](../../templates/weekly-review.md) and [checkpoint](../../templates/checkpoint.md) in your private folder. Never publish children's or customers' private data.

## Adapt and extend

For a lighter workload, meet the same criterion through a conversation, drawing, or synthetic example and split the week across two calendar weeks. For more experience, seek a counterexample or ask another person to test the deliverable; do not automatically add spending, contacts, or tools.

[Back to year 1](../years/year-1.md) · [Templates](../../templates/README.md)
'''
                (ROOT / f'curriculum/lessons/y1-w{w:02d}.md').write_text(text, encoding='utf-8')
        if year > 1:
            parts += ['## How to run each week', '',
                      'Block 1: review evidence and explain the concept (90 minutes). Block 2: build the specified deliverable (90 minutes). '
                      'Block 3: run the proposed test within limits and permissions (90 minutes). Block 4: self-assess, review with an adult, and save a checkpoint (90 minutes). '
                      'Each four-week cycle produces a decision, not a mandatory revenue quota. '
                      'Return to readings and templates as needed; the coach may explain and adapt without inventing evidence.', '']
        (ROOT / f'curriculum/years/year-{year}.md').write_text('\n'.join(parts), encoding='utf-8')


if __name__ == '__main__':
    render()
