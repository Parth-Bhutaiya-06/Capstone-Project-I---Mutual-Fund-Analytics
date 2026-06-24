import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_DIR = BASE_DIR / "data" / "processed"

for file in PROCESSED_DIR.glob("*.csv"):

    df = pd.read_csv(file)

    print("\n"+"="*60)
    print(file.name)

    print("Rows:",len(df))
    print("Columns:",len(df.columns))

    print(
        "Duplicates:",
        df.duplicated().sum()
    )

    print(
        "Null Values:"
    )

    print(df.isnull().sum())