from pathlib import Path
import pandas as pd

out = Path(__file__).parent / "data" / "students.csv"
out.parent.mkdir(parents=True, exist_ok=True)
pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "study_hours": [2.0, 3.5, 1.0, 5.0, 4.0],
    "attendance": [70, 82, 60, 95, 88],
    "result": ["Pass", "Pass", "Fail", "Pass", "Pass"],
}).to_csv(out, index=False)
print(f"Created sample dataset: {out} (5 rows)")
