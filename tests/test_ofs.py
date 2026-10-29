import csv
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import socket

SPEC = importlib.util.spec_from_file_location('ofs', Path(__file__).resolve().parents[1] / 'scripts/ofs.py')
ofs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ofs)


class LedgerTests(unittest.TestCase):
    def calculate(self, rows, **options):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'ledger.csv'
            with path.open('w', newline='', encoding='utf-8') as stream:
                writer = csv.writer(stream)
                writer.writerow(ofs.FIELDS)
                writer.writerows(rows)
            return ofs.cash_indicator(path, **options)

    def row(self, ident, category='revenue', amount='100', mode='real', currency='USD', fx='1'):
        return [ident, '2026-01-01', category, amount, currency, fx, mode, 'private-ref']

    def test_costs_refunds_and_funding_are_distinct(self):
        result = self.calculate([self.row('1'), self.row('2', 'refund', '10'),
                                 self.row('3', 'cogs', '20'), self.row('4', 'opex', '5'),
                                 self.row('5', 'tax', '5'), self.row('6', 'investment', '10000'),
                                 self.row('7', 'loan', '500'), self.row('8', 'owner_draw', '12')])
        self.assertEqual(result['cash_basis_indicator_usd'], '60.00')
        self.assertEqual(result['categories_usd']['investment'], '10000.00')

    def test_simulation_never_inflates_real_numbers(self):
        rows = [self.row('1', amount='10'), self.row('2', amount='999999', mode='simulation')]
        self.assertEqual(self.calculate(rows)['cash_basis_indicator_usd'], '10.00')
        self.assertEqual(self.calculate(rows, simulation=True)['cash_basis_indicator_usd'], '999999.00')

    def test_foreign_exchange_and_share(self):
        result = self.calculate([self.row('1', amount='200', currency='MXN', fx='0.05')], share='0.5')
        self.assertEqual(result['cash_basis_indicator_usd'], '10.00')
        self.assertEqual(result['attributable_indicator_usd'], '5.00')

    def test_loss_and_empty_ledger(self):
        self.assertEqual(self.calculate([self.row('1', 'opex', '25')])['cash_basis_indicator_usd'], '-25.00')
        result = self.calculate([])
        self.assertEqual(result['rows'], 0)
        self.assertIsNone(result['period_start'])

    def test_invalid_amounts_and_fx_stop_calculation(self):
        for value in ('NaN', 'Infinity', '-1', 'abc', ''):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.calculate([self.row('1', amount=value)])
        for currency, fx in [('USD', '2'), ('MXN', ''), ('MXN', '0'), ('MXN', 'NaN')]:
            with self.subTest(currency=currency, fx=fx), self.assertRaises(ValueError):
                self.calculate([self.row('1', currency=currency, fx=fx)])

    def test_duplicate_unknown_category_and_invalid_date(self):
        with self.assertRaises(ValueError):
            self.calculate([self.row('1'), self.row('1')])
        with self.assertRaises(ValueError):
            self.calculate([self.row('1', category='valuation')])
        row = self.row('1'); row[1] = '2026-02-30'
        with self.assertRaises(ValueError):
            self.calculate([row])

    def test_bad_share(self):
        for share in ('0', '-1', '1.01', 'NaN'):
            with self.subTest(share=share), self.assertRaises(ValueError):
                self.calculate([self.row('1')], share=share)


class CurriculumAndPrivacyTests(unittest.TestCase):
    def test_all_weeks_are_addressable(self):
        for year in range(1, 5):
            for week in range(1, 41):
                self.assertTrue(ofs.week_entry(year, week)['criterion'])
        with self.assertRaises(ValueError):
            ofs.week_entry(5, 1)

    def test_alias_rejects_paths_and_hidden_names(self):
        for alias in ('../student', '/tmp/student', '.', '', 'two words', 'a/b'):
            with self.subTest(alias=alias), self.assertRaises(ValueError):
                ofs.safe_alias(alias)

    def test_init_refuses_overwrite_and_complete_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'templates').mkdir()
            for name in ('checkpoint.md', 'family-agreement.md', 'ledger.csv', 'weekly-review.md'):
                (root / 'templates' / name).write_text('template', encoding='utf-8')
            plan = ofs.load_plan()
            with patch.object(ofs, 'ROOT', root), patch.object(ofs, 'load_plan', return_value=plan):
                folder = ofs.init_student('learner')
                with self.assertRaises(FileExistsError):
                    ofs.init_student('learner')
                ofs.mark_progress('learner', 1, 1)
                result = ofs.mark_progress('learner', 1, 1)
                self.assertEqual(result['completed'], ['y1-w01'])
                self.assertTrue((folder / 'checkpoint.md').is_file())

    def test_private_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as other:
            root = Path(tmp)
            (root / 'private').symlink_to(other, target_is_directory=True)
            with patch.object(ofs, 'ROOT', root), self.assertRaises(ValueError):
                ofs.init_student('learner')

    def test_package_sources_exclude_private_and_raw_media(self):
        for path in ofs.package_files():
            relative = path.relative_to(ofs.ROOT)
            self.assertNotIn('private', relative.parts)
            self.assertNotIn(path.suffix, ('.mp4', '.json3', '.webm'))

    def test_normal_reads_and_finance_require_no_network(self):
        with patch.object(socket, 'socket', side_effect=AssertionError('No network allowed')):
            self.assertEqual(ofs.week_entry(1, 1)['week'], 1)
            result = ofs.cash_indicator(ofs.ROOT / 'examples/ledger-demo.csv', simulation=True)
            self.assertEqual(result['cash_basis_indicator_usd'], '500.00')


if __name__ == '__main__':
    unittest.main()
