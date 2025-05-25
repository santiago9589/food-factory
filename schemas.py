from pydantic import BaseModel
from typing import Optional
from datetime import date


#INCIO CLASES DE ENTRADA DE DATOS

class ClientBase(BaseModel):
    name:str
    lastname:str
    dateofbirth:date
    address: str

class ProductBase(BaseModel):
    product_name: str
    description:str
    quantity:int

class ProductUpdateBase(BaseModel):
    id:int
    product_name: str
    description:str
    quantity:int
class ProductUpdateQuantity(BaseModel):
    quantity:int    

class SellerBase(BaseModel):
    name:str
    lastname:str
    dateofbirth:date
    is_online: bool

class SaleBase(BaseModel):
    client:int
    seller:int
    dateofbuy:date
    total: float
    products: list[ProductUpdateBase]

 #FIN CLASES DE ENTRADA DE DATOS   