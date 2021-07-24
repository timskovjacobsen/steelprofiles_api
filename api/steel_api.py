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
            f"""The profile type must be one of the supported types: {PROFILE_TYPES}.
            \n\nYou can request a specific profile, say HEA120, by visiting the endpoint '/api/HEA/120'""",
            status_code=404,
        )

    query = f"SELECT * FROM {profile_type}"
    return _read_db(query)


@router.get("/api/{profile_type}")
def profile_type(profile_type: str) -> Dict:
    f"""Return of all steel profiles present of a certain type in the database.

    Supported profile types are:\n{PROFILE_TYPES}

    Example
    -------
    Visiting the endpoint

        steelapi/timskovjacobsen.com/api/HEA

    returns a JSON response with all HEA profiles and their data.
    """

    profile_type = profile_type.upper()
    try:
        df = _get_all_profiles_from_type(profile_type)
        return _df_to_json(df)
    except ValidationError as e:
        return fastapi.Response(content=e.error_msg, status_code=e.status_code)


@router.get("/api/{profile_type}/{dimension}")
def anyprofile(profile_type: str, dimension: str) -> Dict:
    """Return all the specific profile type with dimension.

    Example
    -------
    Visiting the endpoint

        steelapi/timskovjacobsen.com/api/HEA/120

    returns a JSON response with the data for the HEA120 profile.
    """
    profile_type = profile_type.upper()
    try:
        df = _get_all_profiles_from_type(profile_type)
    except ValidationError as e:
        return fastapi.Response(content=e.error_msg, status_code=e.status_code)

    df = df[df["name"].apply(lambda x: x[3:]) == dimension]

    if df.empty:
        return fastapi.Response(
            content=f"The profile '{profile_type}{dimension}' does not exist.",
            status_code=404,
        )

    return _df_to_json(df)
