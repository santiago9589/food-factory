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
