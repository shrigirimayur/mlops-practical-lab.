# Lightweight SQLite demonstration of reusable feature storage.
# This is a teaching example, not a Feast installation.
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "features.sqlite"

def main():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS customer_features (
                customer_id INTEGER PRIMARY KEY,
                age INTEGER NOT NULL,
                account_age_days INTEGER NOT NULL
            )
        """)
        conn.executemany(
            "INSERT OR REPLACE INTO customer_features VALUES (?, ?, ?)",
            [(1, 20, 100), (2, 25, 500), (3, 31, 900)]
        )
        rows = conn.execute(
            "SELECT customer_id, age, account_age_days FROM customer_features ORDER BY customer_id"
        ).fetchall()
    print("Feature rows retrieved:", len(rows))
    for row in rows:
        print(row)
    print("Note: SQLite demo only; Feast must be configured separately.")

if __name__ == "__main__":
    main()
