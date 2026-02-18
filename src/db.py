import pandas as pd
from sqlalchemy import create_engine
from .config import DB_URL

_engine = create_engine(DB_URL)

def read_table(table_name: str):
    df = pd.read_sql_table(table_name, _engine)
    return pd.read_sql_table(table_name, _engine)