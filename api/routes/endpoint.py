from fastapi import APIRouter,Request
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from sqlalchemy.orm import Session
from datetime import date
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.templating import Jinja2Templates
from fastapi import Form
from database import AsyncSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from typing import AsyncGenerator
from ..client import dal

router = APIRouter()
templates = Jinja2Templates(directory="templates")

#MENU PPAL


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


@router.get("/app/home")
def read_dashboard(request: Request):
    return templates.TemplateResponse("paneldecontrol.html", {"request": request})



#ROOT CLIENTES

@router.get("/app/clients")
def read_dashboard(request: Request):
    return templates.TemplateResponse("panelclients.html", {"request": request})
@router.get("/app/clients/add")
def read_dashboard(request: Request):
    return templates.TemplateResponse("addclients.html", {"request": request})
@router.get("/app/clients/list")
async def read_dashboard(request: Request,db:AsyncSession = Depends(get_db)):
    clients = await dal.getAll(db)
    return templates.TemplateResponse("listclients.html", {"request": request,"clients":clients})



