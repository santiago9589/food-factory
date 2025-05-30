from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, dal 
from database import AsyncSessionLocal


router = APIRouter()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


@router.post("/", response_model=schemas.ClientBase)
async def create(client: schemas.ClientBase, db:AsyncSession = Depends(get_db)):
    return await dal.create_client(db, client)



@router.get("/",response_model=list[schemas.ClientBase])
async def getAll( db:AsyncSession = Depends(get_db)):
    return await dal.get_client(db)



@router.delete("/delete-{id}",response_model=str)
async def deleteOne(id:int,db:AsyncSession = Depends(get_db)):
    return await dal.delete_one(db,id)


#todo update