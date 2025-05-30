from sqlalchemy import String, Integer, Column, Date, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base
from ..client.schemas import Person


# VENDEDOR
class Seller(Person, Base):
    __tablename__ = "table_seller"
    id = Column(Integer, primary_key=True, index=True)
    is_online = Column(Boolean, default=False)
    
    sales = relationship("Sale", back_populates="seller")