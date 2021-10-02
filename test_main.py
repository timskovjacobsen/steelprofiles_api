# Standard library imports
import sqlite3
from pathlib import Path

# Third party imports
import pytest
from starlette.testclient import TestClient
import pandas as pd

# Project imports
from main import api
from api import steel_api

DATABASE_PATH = Path("steelprofiles.db")

client: TestClient = TestClient(
    api
)

supported_profiles = steel_api.PROFILE_TYPES 

def _profiles_dimensions(supported_profiles):

    profiles_dimensions = []
    con = sqlite3.connect(DATABASE_PATH)
    for profile_type in supported_profiles:
        query = f"SELECT SUBSTR(name,1,3), SUBSTR(NAME,4,3) FROM {profile_type}"
        profiles_dimension = pd.read_sql(query, con).values.tolist()
        profiles_dimensions += profiles_dimension
    return profiles_dimensions
 
supported_profiles_dimensions = _profiles_dimensions(supported_profiles)
 
@pytest.mark.parametrize('profile_type', supported_profiles)
def test_profile_type(profile_type) -> None:
    response: Response = client.get(
        '/api/' + profile_type
    )
    assert response.status_code == 200

@pytest.mark.parametrize('profile_type_dimension', supported_profiles_dimensions)
def test_anyprofile(profile_type_dimension) -> None:
    response: Response = client.get(
        '/api/' + profile_type_dimension[0] + '/' + profile_type_dimension[1]
    )
    assert response.status_code == 200
