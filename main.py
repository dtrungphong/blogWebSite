from fastapi import FastAPI, UploadFile, File
from starlette.responses import FileResponse 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi import Request

from pydantic import BaseModel
from typing import Optional, List

templates = Jinja2Templates(directory="static")
app = FastAPI()

# app.mount("/", StaticFiles(directory="static"), name="static")
@app.get("/")
async def home(request: Request):
	return templates.TemplateResponse("/home.html",{"request":request})