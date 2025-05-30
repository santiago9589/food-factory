from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, dal 
from database import AsyncSessionLocal


router = APIRouter()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


@router.post("/", response_model=schemas.ProductBase)
async def create(product: schemas.ProductBase, db:AsyncSession = Depends(get_db)):
    return await dal.create_product(db, product)




