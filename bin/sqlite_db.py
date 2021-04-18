"""Script for creating a SQLite database from csv files."""

# Standard library imports
import sqlite3
from pathlib import Path
from glob import glob

# Third party imports
import pandas as pd

conn = sqlite3.connect("steelprofiles.db")

assets = Path(__file__).parent.parent / "assets"
for f in glob(f"{str(assets)}/*.csv"):
    df = pd.read_csv(f)
    table_name = Path(f).stem
    df.to_sql(table_name, conn, if_exists="replace")

conn.close()
