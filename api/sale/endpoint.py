from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, dal 
from database import AsyncSessionLocal
from ..sale.schemas import SaleResponse,SaleBase

router = APIRouter()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


@router.post("/", response_model=SaleResponse)
async def create(sale: SaleBase, db:AsyncSession = Depends(get_db)):
    return await dal.create_sale(db, sale)


@router.get("/",response_model=list[SaleBase])
async def getAll( db:AsyncSession = Depends(get_db)):
    return await dal.getAll(db)

