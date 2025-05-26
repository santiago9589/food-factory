from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import schemas, dal, database
from database import AsyncSessionLocal


router = APIRouter()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


@router.post("/", response_model=schemas.ClientBase)
async def create(usuario: schemas.ClientBase, db:AsyncSession = Depends(get_db)):
    return await dal.create_client(db, usuario)







