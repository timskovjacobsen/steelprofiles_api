# Standard libray imports
import pandas as pd
import sqlite3
from pathlib import Path

# Third party imports
from fastapi import FastAPI

app = FastAPI()

DATABASE_PATH = Path("steelprofiles.sqlite3")


def _read_db(query: str) -> pd.DataFrame:
    con = sqlite3.connect(DATABASE_PATH)
    return pd.read_sql(query, con)


def _df_to_json(df):
    # Get list of dicts from the dataframe. E.g.:
    # [{name: HEA100, b: 100, ...}, {name: HEA120, b: 120, ...}]
    d = df.to_dict("records")

    # Transform outer list to dict with keys being the name of each profile. E.g.:
    # {HEA100: {name: HEA100, b: 100, ...}, HEA120: {name: HEA120, b: 120, ...}}
    return {subdict["name"]: subdict for subdict in d}


@app.get("/")
async def root():
    """Return a response of all steel profiles."""

    query = """SELECT * FROM HEA"""
    df = _read_db(query)
    return _df_to_json(df)


@app.get("/{profile}")
async def anyprofile(string: str):
    query = """SELECT * FROM HEA"""
    df = _read_db(query)
    df = df[df["name"].str.contains(string)]
    return _df_to_json(df)
