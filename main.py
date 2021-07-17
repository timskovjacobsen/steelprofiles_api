# Standard libray imports
from typing import Dict
import sqlite3
from pathlib import Path

# Third party imports
import fastapi
from fastapi.templating import Jinja2Templates
import uvicorn
from starlette.staticfiles import StaticFiles

# Project imports
from views import home
from api import steel_api


api = fastapi.FastAPI()

templates = Jinja2Templates(directory="templates")


def configure():
    configure_routing()


def configure_routing():
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(home.router)
    api.include_router(steel_api.router)


if __name__ == "__main__":
    # For running in development
    configure()
    uvicorn.run("main:api", port=8000, host="127.0.0.1", reload=True)

else:
    # For running in production
    configure()
