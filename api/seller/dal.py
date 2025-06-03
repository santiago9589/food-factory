from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from . import schemas, models 
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException



async def create_seller(db: AsyncSession, seller:schemas.SellerBase):
    try:
        create_seller = models.Seller(**seller.dict())
        db.add(create_seller)
        await db.commit()
        await db.refresh(create_seller)
        return create_seller
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear al vendedor : {str(e)}")


async def getAll(db: AsyncSession):
    try:
        result = await db.execute(select(models.Seller))
        sellers = result.scalars().all()
        return sellers
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener vendedores: {str(e)}")


async def delete_one(db: AsyncSession, id: int):
    # Verificar si el objeto existe
    result = await db.execute(select(models.Seller).filter(models.Seller.id == id))
    seller = result.scalars().first()

    if not seller:
        raise HTTPException(status_code=404, detail=f"vendedor con ID {id} no encontrado")

    await db.delete(seller)
    await db.commit()
    return "Se borró con éxito"

async def update_one(db:AsyncSession,id:int,newDataseller:schemas.SellerBase):
    # Verificar si el objeto existe
    result = await db.execute(select(models.Seller).filter(models.Seller.id == id))
    seller = result.scalars().first()

    if not seller:
        raise HTTPException(status_code=404, detail=f"vendedor con ID {id} no encontrado")
    
    newDataseller.is_online = seller.is_online
    newDataseller.name = newDataseller.name
    newDataseller.lastname = newDataseller.lastname

    await db.commit()

    return "Se modifico el vendedor con exito"
