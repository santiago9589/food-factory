from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, dal 
from database import AsyncSessionLocal


router = APIRouter()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


@router.post("/", response_model=schemas.SellerBase)
async def create(seller: schemas.SellerBase, db:AsyncSession = Depends(get_db)):
    return await dal.create_seller(db, seller)




