# Cash, profit, and the million-dollar target

Start by explaining these distinctions using your own example:

| Concept | Meaning | Does it count as profit? |
| --- | --- | --- |
| Collected sale | Money received for delivering something | Only after costs and adjustments |
| Booking or unpaid invoice | Commitment or future receipt | Not in the cash-basis ledger |
| Investment/loan | Financing | No |
| Valuation | Estimated company value | No |
| Owner withdrawal | Movement to the owner's personal account | Not a new operating expense |
| Profit | Economic result after costs | Specify period and accounting basis |

## Educational ledger

`templates/ledger.csv` uses positive amounts and one category per row: `revenue`, `refund`, `cogs`, `opex`, `tax`, `investment`, `loan`, `owner_draw`, `transfer`. The category determines the sign. Do not enter a negative refund: that would subtract it twice. Use a unique ID, ISO date, currency, anonymous evidence reference, and `real` or `simulation`.

`usd_per_unit` means how many US dollars one unit of that row's currency is worth. For USD it must equal 1. For MXN, use an adult-documented exchange rate in the reference; the tool does not look up exchange rates or verify they are current. Never mix amounts without conversion or choose rates to reach the target.

Educational USD cash-basis indicator = `revenue` receipts − `refund` − `cogs` − `opex` − `tax`. Financing, withdrawals, and transfers are shown separately and do not change that indicator. Only `real` rows count by default; `--simulation` calculates simulated rows exclusively.

This indicator does not resolve inventory, depreciation, accruals, personal taxes, or consolidation across businesses. Record missing costs even if the business is losing money. Include paid third-party work and AI. Track student hours separately and consider a hypothetical time cost when evaluating viability, without confusing it with a recorded payment.

## Fictional example

Sales US$1,000; refunds US$50; direct costs US$300; operations US$100; recorded taxes US$50: indicator US$500. A US$10,000 investment does not make it US$10,500. A US$1M valuation does not change it either. If taxes or costs remain unknown, label the result provisional.

See `examples/ledger-demo.csv` and run `python3 scripts/ofs.py profit examples/ledger-demo.csv --simulation`. Do not upload receipts or bank data to this repository. Keep supporting evidence privately with adult review. Before any public net-profit claim, reconcile the records with a competent person.
