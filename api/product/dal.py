from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from . import schemas, models 
from ..product.models import Product
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError



async def create_product(db: AsyncSession, product:schemas.ProductBase):

    try:
        new_product = Product(**product.dict())
        db.add(new_product)
        await db.commit()
        await db.refresh(new_product)
        return new_product
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear producto: {str(e)}")



async def getAll(db: AsyncSession):
    try:
        result = await db.execute(select(Product))
        products = result.scalars().all()
        return products
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener productos: {str(e)}")
    

async def delete_one(db: AsyncSession, id: int):
    # Verificar si el objeto existe
    result = await db.execute(select(Product).filter(Product.id == id))
    product = result.scalars().first()

    if not product:
        raise HTTPException(status_code=404, detail=f"Producto con ID {id} no encontrado")

    await db.delete(product)
    await db.commit()
    return "Se borró con éxito"



async def update_one(db:AsyncSession,id:int,newDataProduct:Product):
    # Verificar si el objeto existe
    result = await db.execute(select(Product).filter(Product.id == id))
    producto = result.scalars().first()

    if not producto:
        raise HTTPException(status_code=404, detail=f"Producto con ID {id} no encontrado")
    
    producto.product_name = newDataProduct.product_name
    producto.description = newDataProduct.description
    producto.quantity = newDataProduct.quantity

    await db.commit()

    return "Se modifico el cliente con exito"



async def update_quantity(db: AsyncSession, product:schemas.ProductBase,quantity:int):
    result = await db.execute(select(Product).filter(Product.id == product.id))
    product_found = result.scalars().first()

    # Validar existencia
    if not product_found:
        raise HTTPException(status_code=404, detail=f"Producto con ID {product.id} no encontrado")

    # Validar stock suficiente
    if product_found.quantity < quantity:
        raise HTTPException(status_code=400, detail="Stock insuficiente")

    # Actualizar cantidad
    product_found.quantity -= quantity

    # Guardar cambios
    await db.commit()
    await db.refresh(product_found)

    return product_found