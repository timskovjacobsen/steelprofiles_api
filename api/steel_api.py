# Standard library imports
from models.validation_error import ValidationError
from typing import Dict
from pathlib import Path
import sqlite3

# Third party imports
import fastapi
from fastapi import Depends
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from starlette.templating import Jinja2Templates
import pandas as pd


router = fastapi.APIRouter()

templates = Jinja2Templates("templates")

DATABASE_PATH = Path("steelprofiles.db")
PROFILE_TYPES = ["HEA", "HEB", "HEM", "IPE", "IPN", "UPN"]


def _read_db(query: str) -> pd.DataFrame:
    con = sqlite3.connect(DATABASE_PATH)
    return pd.read_sql(query, con)


def _df_to_json(df: pd.DataFrame) -> Dict[str, Dict[str, str]]:
    # Get list of dicts from the dataframe. E.g.:
    # [{name: HEA100, b: 100, ...}, {name: HEA120, b: 120, ...}]
    d = df.to_dict("records")

    # Transform outer list to dict with keys being the name of each profile. E.g.:
    # {HEA100: {name: HEA100, b: 100, ...}, HEA120: {name: HEA120, b: 120, ...}}
    return {subdict["name"]: subdict for subdict in d}


def _get_all_profiles_from_type(profile_type: str):

    if profile_type not in PROFILE_TYPES:
        raise ValidationError(
            f"The profile type must be one of the supported types: {PROFILE_TYPES}.",
            status_code=404,
        )

    query = f"SELECT * FROM {profile_type}"
    return _read_db(query)


@router.get("/{profile_type}")
def profile_type(profile_type: str) -> Dict:
    """Return of all steel profiles present of a certain type in the database."""

    try:
        df = _get_all_profiles_from_type(profile_type)
        return _df_to_json(df)
    except ValidationError as e:
        return fastapi.Response(content=e.error_msg, status_code=e.status_code)


@router.get("/{profile_type}/{match_string}")
def anyprofile(profile_type: str, match_string: str) -> Dict:
    """Return all steel profiles whose name contain the given string."""
    try:
        df = _get_all_profiles_from_type(profile_type)
    except ValidationError as e:
        return fastapi.Response(content=e.error_msg, status_code=e.status_code)
    df = df[df["name"].str.contains(match_string)]
    return _df_to_json(df)
