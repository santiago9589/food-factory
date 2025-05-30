from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from . import schemas, models 
from ..product.models import Product
from fastapi import HTTPException



async def create_product(db: AsyncSession, product:schemas.ProductBase):
    new_product = models.Product(**product.dict())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product


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