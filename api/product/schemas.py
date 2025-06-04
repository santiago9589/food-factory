from pydantic import BaseModel
from typing import Optional
from datetime import date



class ProductBase(BaseModel):
    product_name: str
    description:str
    quantity:int

    class Config:
        orm_mode = True


class ProductUpdateBase(BaseModel):
    id:int
    product_name: str
    description:str
    quantity:int

    class Config:
        orm_mode = True

class ProductUpdateQuantity(BaseModel):
    quantity:int 

    class Config:
        from_attributes = True  