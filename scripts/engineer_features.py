from pathlib import Path
import pandas as pd
src = Path('data/processed/customers_clean.csv')
out = Path('data/features/customer_features.csv')
out.parent.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(src)
df['spend_per_visit'] = (df['monthly_spend'] / df['visits_30d'].clip(lower=1)).round(2)
df['high_engagement'] = (df['visits_30d'] >= 8).astype(int)
df['age_band'] = pd.cut(df['age'], bins=[17, 25, 40, 60, 100], labels=['18-25','26-40','41-60','61+']).astype(str)
df.to_csv(out, index=False)
print(f'PASS: engineered 3 features for {len(df)} customers -> {out}')
print(df[['customer_id','spend_per_visit','high_engagement','age_band']].to_string(index=False))
