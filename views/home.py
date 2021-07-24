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


@router.get("/api", include_in_schema=False)
def api_index(request: Request):
    return index(request)


@router.get("/favicon.ico", include_in_schema=False)
def favicon():
    return fastapi.responses.RedirectResponse(url="/static/img/favicon.ico")
