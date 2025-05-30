from sqlalchemy import String, Integer, Column, Date, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base




class SellProduct(Base):
    __tablename__ = "table_sell_product"
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)

    # ForeignKeys
    product_id = Column(Integer, ForeignKey("table_product.id"))
    sale_id = Column(Integer, ForeignKey("table_sale.id"))

    # Relaciones
    product = relationship("Product", back_populates="sales")
    sale = relationship("Sale", back_populates="products")


# VENTA
class Sale(Base):
    __tablename__ = "table_sale"
    id = Column(Integer, primary_key=True, index=True)
    dateofBuy = Column(Date) 
    total = Column(Float)

    seller_id = Column(Integer, ForeignKey("table_seller.id"))
    seller = relationship("Seller", back_populates="sales",lazy="selectin")

    client_id = Column(Integer, ForeignKey("table_client.id"))
    client = relationship("Client", back_populates="sales",lazy="selectin")

    # Relación con SellProduct (intermedia)
    products = relationship("SellProduct", back_populates="sale", cascade="all, delete-orphan",lazy="selectin")