from sqlalchemy import String, Integer, Column, Date, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

# Clase base no mapeada (solo atributos comunes)
class Person:
    name = Column(String(11))
    lastname = Column(String(11))
    dateofbirth = Column(Date)

# CLIENTE
class Client(Person, Base):
    __tablename__ = "table_client"
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String(11))
    
    sales = relationship("Sale", back_populates="client")

# VENDEDOR
class Seller(Person, Base):
    __tablename__ = "table_seller"
    id = Column(Integer, primary_key=True, index=True)
    is_online = Column(Boolean, default=False)
    
    sales = relationship("Sale", back_populates="seller")

# PRODUCTO
class Product(Base):
    __tablename__ = "table_product"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(50))
    description = Column(String(50))
    quantity = Column(Integer)

    # Relación con SellProduct (intermedia)
    sales = relationship("SellProduct", back_populates="product")

# VENTA
class Sale(Base):
    __tablename__ = "table_sale"
    id = Column(Integer, primary_key=True, index=True)
    dateofBuy = Column(Date) 
    total = Column(Float)

    seller_id = Column(Integer, ForeignKey("table_seller.id"))
    seller = relationship("Seller", back_populates="sales")

    client_id = Column(Integer, ForeignKey("table_client.id"))
    client = relationship("Client", back_populates="sales")

    # Relación con SellProduct (intermedia)
    products = relationship("SellProduct", back_populates="sale", cascade="all, delete-orphan")

# VENTA-PRODUCTO (Tabla intermedia)
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






