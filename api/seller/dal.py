from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from . import schemas, models 




async def create_seller(db: AsyncSession, seller:schemas.SellerBase):
    new_seller = models.Seller(**seller.dict())
    db.add(new_seller)
    await db.commit()
    await db.refresh(new_seller)
    
    return new_seller
