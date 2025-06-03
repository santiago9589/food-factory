from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from fastapi import HTTPException
from ..client.models import Client
from sqlalchemy.exc import SQLAlchemyError
from ..client.schemas import ClientBase

async def create_client(db: AsyncSession, client: ClientBase):
    try:
        new_client = Client(**client.dict())
        db.add(new_client)
        await db.commit()
        await db.refresh(new_client)
        return new_client
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear cliente: {str(e)}")


async def getAll(db: AsyncSession):
    try:
        result = await db.execute(select(Client))
        clients = result.scalars().all()
        return clients
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener clientes: {str(e)}")


async def delete_one(db: AsyncSession, id: int):
    # Verificar si el objeto existe
    result = await db.execute(select(Client).filter(Client.id == id))
    client = result.scalars().first()

    if not client:
        raise HTTPException(status_code=404, detail=f"Cliente con ID {id} no encontrado")

    await db.delete(client)
    await db.commit()
    return "Se borró con éxito"

async def update_one(db:AsyncSession,id:int,newDataClient:ClientBase):
    # Verificar si el objeto existe
    result = await db.execute(select(Client).filter(Client.id == id))
    client = result.scalars().first()

    if not client:
        raise HTTPException(status_code=404, detail=f"Cliente con ID {id} no encontrado")
    
    client.address = newDataClient.address
    client.name = newDataClient.name
    client.lastname = newDataClient.lastname

    await db.commit()

    return "Se modifico el cliente con exito"




