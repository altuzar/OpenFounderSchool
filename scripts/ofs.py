#!/usr/bin/env python3
"""OpenFounderSchool offline tooling. No external dependencies or network calls."""
import argparse
import csv
from datetime import date
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PLATFORMS = ('grok-bot', 'claude-project', 'chatgpt-work', 'pi', 'hermes')
CATEGORIES = ('revenue', 'refund', 'cogs', 'opex', 'tax', 'investment', 'loan', 'owner_draw', 'transfer')
FIELDS = ('id', 'date', 'category', 'amount', 'currency', 'usd_per_unit', 'mode', 'evidence')


def load_plan():
    return json.loads((ROOT / 'curriculum/plan.json').read_text(encoding='utf-8'))


def week_entry(year, week):
    for entry in load_plan()['entries']:
        if (entry['year'], entry['week']) == (year, week):
            return entry
    raise ValueError('Unknown year/week: use year 1–4 and week 1–40.')


def safe_alias(alias):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,39}', alias):
        raise ValueError('Invalid alias: use 1–40 ASCII letters, numbers, hyphens, or underscores.')
    return alias


def init_student(alias):
    alias = safe_alias(alias)
    private_root = ROOT / 'private'
    if private_root.is_symlink():
        raise ValueError('private/ cannot be a symbolic link.')
    private_root.mkdir(exist_ok=True)
    folder = private_root / alias
    folder.mkdir(exist_ok=False)
    for name in ('checkpoint.md', 'family-agreement.md', 'ledger.csv', 'weekly-review.md'):
        (folder / name).write_bytes((ROOT / 'templates' / name).read_bytes())
    state = {'alias': alias, 'year': 1, 'week': 1, 'mode': 'simulation', 'completed': []}
    (folder / 'progress.json').write_text(json.dumps(state, indent=2) + '\n', encoding='utf-8')
    return folder


def mark_progress(alias, year, week):
    week_entry(year, week)
    folder = ROOT / 'private' / safe_alias(alias)
    path = folder / 'progress.json'
    if path.is_symlink() or folder.is_symlink() or (ROOT / 'private').is_symlink():
        raise ValueError('The private path cannot contain symbolic links.')
    state = json.loads(path.read_text(encoding='utf-8'))
    if state.get('alias') != alias:
        raise ValueError('The progress file alias does not match.')
    completed = state.setdefault('completed', [])
    key = f'y{year}-w{week:02d}'
    if key not in completed:
        completed.append(key)
    state['year'], state['week'] = year, week
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return state


def number(value, label, positive=False):
    try:
        result = Decimal(value)
    except (InvalidOperation, TypeError):
        raise ValueError(f'{label}: invalid decimal number.') from None
    if not result.is_finite() or result < 0 or result > Decimal('1e15'):
        raise ValueError(f'{label}: must be finite, nonnegative, and at most 1e15.')
    if positive and result == 0:
        raise ValueError(f'{label}: must be greater than zero.')
    return result


def cash_indicator(path, simulation=False, share='1'):
    share_value = number(share, 'participation', positive=True)
    if share_value > 1:
        raise ValueError('Participation must be greater than 0 and at most 1.')
    totals = {key: Decimal('0') for key in CATEGORIES}
    selected = []
    ids = set()
    mode = 'simulation' if simulation else 'real'
    with Path(path).open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != list(FIELDS):
            raise ValueError('Invalid header: use templates/ledger.csv exactly.')
        for index, row in enumerate(reader, 2):
            if None in row or any(row.get(key) is None for key in FIELDS):
                raise ValueError(f'Row {index}: incorrect number of columns.')
            row = {key: value.strip() for key, value in row.items()}
            ident = row['id']
            if not ident or ident in ids:
                raise ValueError(f'Row {index}: empty or duplicate ID.')
            ids.add(ident)
            if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', row['date']):
                raise ValueError(f'Row {index}: date must be YYYY-MM-DD.')
            date.fromisoformat(row['date'])
            if row['category'] not in CATEGORIES or row['mode'] not in ('real', 'simulation'):
                raise ValueError(f'Row {index}: invalid category or mode.')
            if not re.fullmatch(r'[A-Z]{3}', row['currency']) or not row['evidence']:
                raise ValueError(f'Row {index}: invalid currency or evidence reference.')
            amount = number(row['amount'], f'Row {index} amount')
            fx = number(row['usd_per_unit'], f'Row {index} usd_per_unit', positive=True)
            if row['currency'] == 'USD' and fx != 1:
                raise ValueError(f'Row {index}: USD requires usd_per_unit=1.')
            if row['mode'] == mode:
                totals[row['category']] += amount * fx
                selected.append(row['date'])
    indicator = totals['revenue'] - sum(totals[k] for k in ('refund', 'cogs', 'opex', 'tax'))

    def money(value):
        return str(value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

    return {'mode': mode, 'rows': len(selected), 'currency': 'USD',
            'period_start': min(selected) if selected else None,
            'period_end': max(selected) if selected else None,
            'categories_usd': {k: money(v) for k, v in totals.items()},
            'cash_basis_indicator_usd': money(indicator), 'share': str(share_value),
            'attributable_indicator_usd': money(indicator * share_value),
            'notice': 'Educational cash-basis indicator; not audited net profit, goal certification, or accounting advice. Check missing costs.'}


def package_files():
    names = ['README.md', 'README.en.md', 'START-HERE.md', 'AGENTS.md',
             'LICENSE', 'NOTICE.md', 'CONTRIBUTING.md', 'SECURITY.md']
    folders = ['curriculum', 'docs', 'mentors', 'prompts', 'templates', 'adapters',
               'examples', 'scripts', 'tests', 'research', '.pi/prompts']
    paths = [ROOT / n for n in names]
    for folder in folders:
        paths += [p for p in (ROOT / folder).rglob('*') if p.is_file()
                  and p.suffix in ('.md', '.json', '.csv', '.py') and '__pycache__' not in p.parts]
    for path in sorted(set(paths)):
        if (path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(ROOT)
                or any(parent.is_symlink() for parent in path.parents if parent.is_relative_to(ROOT))):
            raise ValueError(f'Unsafe or missing package file: {path.name}')
        if 'private' in path.relative_to(ROOT).parts or 'raw' in path.relative_to(ROOT).parts:
            raise ValueError('Packages cannot include private data or complete third-party source materials.')
        yield path


def packaged_source(name, content):
    if name == 'README.md':
        return content.replace(b'[release](release/README.md)', b'[SETUP](SETUP.md)')
    return content


def pack():
    folder = ROOT / 'release'
    folder.mkdir(exist_ok=True)
    common = {str(p.relative_to(ROOT)): packaged_source(str(p.relative_to(ROOT)), p.read_bytes()) for p in package_files()}
    outputs = []
    for platform in PLATFORMS:
        starter_names = ['prompts/COACH.md', 'docs/SAFETY.md', 'curriculum/OVERVIEW.md',
                         'docs/ASSESSMENT.md', 'mentors/roles.md', 'curriculum/lessons/y1-w01.md']
        starter = '# OpenFounderSchool — starter kit\n\n'
        starter += 'Original material. Tuition and maximum refund US$0; no earnings guarantee. '
        starter += 'Initial mode: SIMULATION. Load further units only when needed.\n\n'
        for name in starter_names:
            # Embedded files have different relative-link bases. Use plain canonical paths.
            content = common[name].decode('utf-8')
            content = re.sub(r'\[([^\]]+)\]\((?!https?://|#)([^)]+)\)', r'\1', content)
            starter += f'\n\n---\n\n## File: {name}\n\n' + content
        payload = dict(common)
        payload['STARTER.md'] = starter.encode('utf-8')
        setup = common[f'adapters/{platform}.md'].decode('utf-8')
        setup = re.sub(r'\[([^\]]+)\]\((?!https?://|#)([^)]+)\)', r'\1', setup)
        payload['SETUP.md'] = setup.encode('utf-8')
        manifest = {'version': '0.2.0', 'platform': platform, 'date': '2026-10-28',
                    'files': {name: hashlib.sha256(content).hexdigest() for name, content in sorted(payload.items())}}
        payload['MANIFEST.json'] = (json.dumps(manifest, indent=2) + '\n').encode('utf-8')
        target = folder / f'openfounderschool-{platform}.zip'
        # Stored entries avoid zlib-version differences across Python installations.
        with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_STORED) as archive:
            for name, content in sorted(payload.items()):
                info = zipfile.ZipInfo(name, date_time=(2026, 10, 28, 0, 0, 0))
                info.compress_type = zipfile.ZIP_STORED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, content)
        outputs.append(target)
    (folder / 'SHA256SUMS').write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in outputs), encoding='utf-8')
    return outputs


def check():
    errors = []
    data = load_plan()
    seen = set()
    for e in data['entries']:
        key = e['year'], e['week']
        if key in seen:
            errors.append(f'Duplicate week {key}')
        seen.add(key)
        for field in ('title', 'concept', 'build', 'test', 'artifact', 'criterion'):
            if not isinstance(e.get(field), str) or not e[field].strip():
                errors.append(f'Empty field {key}: {field}')
    expected = {(year, week) for year in range(1, 5) for week in range(1, 41)}
    if seen != expected or data.get('hours_per_week') != 6:
        errors.append('Expected 160 weeks and six hours per week.')
    for w in range(1, 41):
        if not (ROOT / f'curriculum/lessons/y1-w{w:02d}.md').is_file():
            errors.append(f'Missing lesson {w}')
    for path in ROOT.rglob('*.md'):
        if any(part in path.relative_to(ROOT).parts for part in ('private', '.git', '__pycache__')):
            continue
        for raw in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            if raw.startswith(('http://', 'https://', '#', 'mailto:')):
                continue
            target = raw.split('#', 1)[0]
            if target and not (path.parent / target).exists():
                errors.append(f'Broken local link: {path.relative_to(ROOT)} -> {target}')
    for platform in PLATFORMS:
        target = ROOT / f'release/openfounderschool-{platform}.zip'
        if not target.exists():
            continue  # Initial source checkout can be validated before packaging.
        with zipfile.ZipFile(target) as archive:
            manifest = json.loads(archive.read('MANIFEST.json'))
            if set(archive.namelist()) != set(manifest['files']) | {'MANIFEST.json'}:
                errors.append(f'Invalid package inventory: {platform}')
            for name, digest in manifest['files'].items():
                if name.startswith('/') or '..' in Path(name).parts or 'private' in Path(name).parts:
                    errors.append(f'Unsafe package path: {name}')
                if hashlib.sha256(archive.read(name)).hexdigest() != digest:
                    errors.append(f'Invalid checksum: {name}')
                source = ROOT / name
                if name not in ('STARTER.md', 'SETUP.md') and (not source.is_file() or packaged_source(name, source.read_bytes()) != archive.read(name)):
                    errors.append(f'Outdated package: {platform}/{name}')
                if name.endswith('.md'):
                    for raw in re.findall(r'\[[^\]]*\]\(([^)]+)\)', archive.read(name).decode('utf-8')):
                        if raw.startswith(('https://', 'http://', 'mailto:', '#')):
                            continue
                        target_path = raw.split('#', 1)[0]
                        # Resolve POSIX relative paths without touching the filesystem.
                        import posixpath
                        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), target_path))
                        if target_path and resolved not in archive.namelist():
                            errors.append(f'Broken link inside {platform}: {name} -> {raw}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    p = commands.add_parser('init'); p.add_argument('--alias', required=True)
    p = commands.add_parser('lesson'); p.add_argument('--year', type=int, required=True); p.add_argument('--week', type=int, required=True)
    p = commands.add_parser('complete'); p.add_argument('--alias', required=True); p.add_argument('--year', type=int, required=True); p.add_argument('--week', type=int, required=True)
    p = commands.add_parser('profit'); p.add_argument('ledger', type=Path); p.add_argument('--simulation', action='store_true'); p.add_argument('--share', default='1')
    commands.add_parser('pack'); commands.add_parser('check')
    args = parser.parse_args()
    try:
        if args.command == 'init':
            print(init_student(args.alias))
        elif args.command == 'lesson':
            e = week_entry(args.year, args.week)
            if args.year == 1:
                print((ROOT / f'curriculum/lessons/y1-w{args.week:02d}.md').read_text(encoding='utf-8'))
            else:
                print(json.dumps(e, ensure_ascii=False, indent=2))
        elif args.command == 'complete':
            print(json.dumps(mark_progress(args.alias, args.year, args.week), ensure_ascii=False, indent=2))
            print('Self-reported progress; not human assessment or certification of results.')
        elif args.command == 'profit':
            print(json.dumps(cash_indicator(args.ledger, args.simulation, args.share), ensure_ascii=False, indent=2))
        elif args.command == 'pack':
            for path in pack():
                print(path.relative_to(ROOT))
        elif args.command == 'check':
            errors = check()
            if errors:
                print('\n'.join(errors), file=sys.stderr)
                return 1
            print('OK: 160 weeks, 40 lessons, local links, and existing packages.')
    except (ValueError, OSError, KeyError, InvalidOperation, zipfile.BadZipFile) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
