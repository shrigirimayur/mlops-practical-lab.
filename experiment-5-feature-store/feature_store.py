from pathlib import Path
import sqlite3, subprocess, sys
ROOT = Path(__file__).resolve().parents[1]
features_csv = ROOT / 'data/features/customer_features.csv'
if not features_csv.exists():
    subprocess.run([sys.executable, str(ROOT/'scripts/generate_dataset.py')], check=True, cwd=ROOT)
    subprocess.run([sys.executable, str(ROOT/'scripts/preprocess_data.py')], check=True, cwd=ROOT)
    subprocess.run([sys.executable, str(ROOT/'scripts/engineer_features.py')], check=True, cwd=ROOT)
import pandas as pd
rows = pd.read_csv(features_csv)
db_path = Path(__file__).with_name('feature_store.db')
with sqlite3.connect(db_path) as con:
    con.execute("""CREATE TABLE IF NOT EXISTS feature_values (
        entity_id INTEGER NOT NULL, feature_name TEXT NOT NULL,
        feature_value TEXT NOT NULL, event_time TEXT NOT NULL,
        PRIMARY KEY(entity_id, feature_name, event_time))""")
    now = '2026-10-14T00:00:00Z'  # fixed demo timestamp for repeatable output
    for _, row in rows.iterrows():
        for name in ['spend_per_visit','high_engagement','age_band']:
            con.execute('INSERT OR REPLACE INTO feature_values VALUES (?, ?, ?, ?)',
                        (int(row['customer_id']), name, str(row[name]), now))
    print('Feature store schema: feature_values(entity_id, feature_name, feature_value, event_time)')
    result = con.execute('SELECT entity_id, feature_name, feature_value FROM feature_values WHERE entity_id=? ORDER BY feature_name', (1002,)).fetchall()
    print('Retrieved features for entity 1002:')
    for item in result: print(item)
    count = con.execute('SELECT COUNT(*) FROM feature_values').fetchone()[0]
    print(f'PASS: {count} feature values available in {db_path.name}')
