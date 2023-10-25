import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
from pydantic import BaseModel
import datetime as dt
from dotenv import load_dotenv
from geosyspy.geosys import Region,Env
import json
from {{cookiecutter.project_slug}}.processor import {{cookiecutter.__processor_class_name}}

app = FastAPI(
    docs_url=None,
    title="{{cookiecutter.project_name}}"+" API",
    description= "{{cookiecutter.description}}"
    )
app.mount("/static", StaticFiles(directory="./api/files"), name="static")

@app.get("/docs", include_in_schema=False)
async def swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="{{cookiecutter.project_name}}"+" API",
        swagger_favicon_url="/static/favicon.svg"
    )
