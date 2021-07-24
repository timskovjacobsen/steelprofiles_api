import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates
import pandas as pd

# Template object for managing all templates
templates = Jinja2Templates("templates")
router = fastapi.APIRouter()


@router.get("/", include_in_schema=False)
def index(request: Request):
    return templates.TemplateResponse(
        "home/index.html",
        {"request": request},
    )


@router.get("/favicon.ico", include_in_schema=False)
def favicon():
    return fastapi.responses.RedirectResponse(url="/static/img/favicon.ico")


@router.get("/HEA", include_in_schema=False)
def HEA(request: Request):

    df = pd.read_csv("./assets/HEA.csv")
    df_html = df.to_html()

    return templates.TemplateResponse(
        "home/profiletable.html",
        {"request": request, "df_html": df_html, "profile_type": "HEA"},
    )


@router.get("/hea", include_in_schema=False)
def hea(request: Request):
    """Alias for '/HEA' endpoint to make enable lower case usage in URL."""
    return HEA(request)
