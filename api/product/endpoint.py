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



@router.get("/",response_model=list[schemas.ProductUpdateBase])
async def getAll( db:AsyncSession = Depends(get_db)):
    return await dal.getAll(db)



@router.delete("/delete-{id}",response_model=str)
async def deleteOne(id:int,db:AsyncSession = Depends(get_db)):
    return await dal.delete_one(db,id)


@router.put("/update-{id}",response_model=str)
async def updateOne(product: schemas.ProductBase,id:int,db:AsyncSession = Depends(get_db)):
    return await dal.update_one(db,id,product)
