from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
import models, schemas




async def create_client(db: AsyncSession, client:schemas.ClientBase):
    new_client = models.Client(**client.dict())
    db.add(new_client)
    await db.commit()
    await db.refresh(new_client)
    return new_client
