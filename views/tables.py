# Standard Library imports
from typing import List

# Third party imports
import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates
import pandas as pd

# Project imports
from api import steel_api


# Template object for managing all templates
templates = Jinja2Templates("templates")
router = fastapi.APIRouter()


def _create_profile_table_endpoint(profile_type: str):
    """Generate functions representing endpoints upper and lower case url strings."""

    @router.get(f"/{profile_type.upper()}", include_in_schema=False)
    def uppercase_profile_endpoint_template(request: Request):

        df = pd.read_csv(f"./assets/{profile_type}.csv")
        df_html = df.to_html()

        return templates.TemplateResponse(
            "home/profiletable.html",
            {"request": request, "df_html": df_html, "profile_type": profile_type},
        )

    @router.get(f"/{profile_type.lower()}")
    def lowercase_profile_endpoint_template(request: Request):
        return uppercase_profile_endpoint_template(request)

    return uppercase_profile_endpoint_template, lowercase_profile_endpoint_template


def _create_all_profile_table_endpoints(all_profile_types: List[str]):
    """Generate endpoints for all supported profiles."""

    for profile in all_profile_types:
        _create_profile_table_endpoint(profile)


# Driver code for endpoint generation
_create_all_profile_table_endpoints(steel_api.PROFILE_TYPES)
