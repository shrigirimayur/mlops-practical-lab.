from pathlib import Path
import csv

out = Path('data/raw/customers.csv')
out.parent.mkdir(parents=True, exist_ok=True)
rows = [
    {'customer_id': 1001, 'age': 21, 'monthly_spend': 1200.0, 'visits_30d': 5, 'churned': 0},
    {'customer_id': 1002, 'age': 34, 'monthly_spend': 2500.0, 'visits_30d': 12, 'churned': 0},
    {'customer_id': 1003, 'age': 29, 'monthly_spend': 800.0, 'visits_30d': 2, 'churned': 1},
    {'customer_id': 1004, 'age': 45, 'monthly_spend': 3200.0, 'visits_30d': 15, 'churned': 0},
    {'customer_id': 1005, 'age': 26, 'monthly_spend': 950.0, 'visits_30d': 3, 'churned': 1},
    {'customer_id': 1006, 'age': 39, 'monthly_spend': 2100.0, 'visits_30d': 9, 'churned': 0},
    {'customer_id': 1007, 'age': 31, 'monthly_spend': 1750.0, 'visits_30d': 7, 'churned': 0},
    {'customer_id': 1008, 'age': 52, 'monthly_spend': 600.0, 'visits_30d': 1, 'churned': 1},
]
with out.open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader(); w.writerows(rows)
print(f'PASS: generated {len(rows)} rows -> {out}')
