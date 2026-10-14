from pathlib import Path
import pandas as pd
src = Path('data/raw/customers.csv')
out = Path('data/processed/customers_clean.csv')
out.parent.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(src)
required = {'customer_id', 'age', 'monthly_spend', 'visits_30d', 'churned'}
missing = required - set(df.columns)
if missing:
    raise ValueError(f'Missing required columns: {sorted(missing)}')
if df['customer_id'].isna().any() or df['customer_id'].duplicated().any():
    raise ValueError('customer_id must be present and unique')
for c in ['age', 'monthly_spend', 'visits_30d', 'churned']:
    df[c] = pd.to_numeric(df[c], errors='raise')
if not df['age'].between(18, 100).all(): raise ValueError('age outside allowed range')
if (df['monthly_spend'] < 0).any() or (df['visits_30d'] < 0).any(): raise ValueError('negative values are invalid')
if not df['churned'].isin([0,1]).all(): raise ValueError('churned must be 0 or 1')
df = df.drop_duplicates().sort_values('customer_id')
df.to_csv(out, index=False)
print(f'PASS: validated and cleaned {len(df)} rows -> {out}')
