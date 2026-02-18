import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

DB = dict(host="localhost", port=5432, database="homecredit", user="mluser", password="mlpassword")

def engine():
    return create_engine(f"postgresql+psycopg2://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}")

def create_table_from_sample(csv_path: Path, table_name: str, nrows: int = 200):
    df = pd.read_csv(csv_path, nrows=nrows)
    df.head(0).to_sql(table_name, engine(), if_exists="replace", index=False)

def copy_into_table(container_csv_path: str, table_name: str):
    # COPY runs on the DB server side, so it needs the container path (/data/raw/..)
    conn = psycopg2.connect(**DB)
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute(f"COPY {table_name} FROM '{container_csv_path}' WITH (FORMAT csv, HEADER true)")
    conn.close()

def load_csv_fast(csv_filename: str):
    csv_path = RAW_DIR / csv_filename
    table = csv_filename.replace(".csv", "").lower()
    print(f"\n==> {csv_filename} -> {table}")

    create_table_from_sample(csv_path, table)
    container_path = f"/data/raw/{csv_filename}"
    copy_into_table(container_path, table)

    print("Loaded.")

if __name__ == "__main__":
    files = [
        "application_train.csv",
        "application_test.csv",
        "previous_application.csv",
        "credit_card_balance.csv",
        "installments_payments.csv",
        "POS_CASH_balance.csv",
    ]
    for f in files:
        load_csv_fast(f)
