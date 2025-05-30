from sqlalchemy import String, Integer, Column, Date, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base


# PRODUCTO
class Product(Base):
    __tablename__ = "table_product"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(50))
    description = Column(String(50))
    quantity = Column(Integer)

    # Relación con SellProduct (intermedia)
    sales = relationship("SellProduct", back_populates="product")