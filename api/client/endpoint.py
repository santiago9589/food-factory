from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, dal 
from database import AsyncSessionLocal
from fastapi import Form

router = APIRouter()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


@router.post("/", response_model=schemas.ClientBase)
async def create(
    name: str = Form(...),
    lastname: str = Form(...),
    dateofbirth: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    client_data = schemas.ClientBase(name=name, lastname=lastname, dateofbirth=dateofbirth)
    return await dal.create_client(db, client_data)



@router.get("/",response_model=list[schemas.ClientBase])
async def getAll( db:AsyncSession = Depends(get_db)):
    return await dal.getAll(db)



@router.delete("/delete-{id}",response_model=str)
async def deleteOne(id:int,db:AsyncSession = Depends(get_db)):
    return await dal.delete_one(db,id)


@router.put("/update-{id}",response_model=str)
async def updateOne(client: schemas.ClientBase,id:int,db:AsyncSession = Depends(get_db)):
    return await dal.update_one(db,id,client)