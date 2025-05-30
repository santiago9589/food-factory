from pydantic import BaseModel
from typing import Optional
from datetime import date
from ..product.schemas import ProductUpdateBase

class SaleBase(BaseModel):
    client:int
    seller:int
    dateofBuy:date
    total: float
    products: list[ProductUpdateBase]

    class Config:
        orm_mode = True


class SaleResponse(BaseModel):
    sale_id: int
    dateofBuy: date
    total: float
    seller: int  # O más información si quieres
    client: int
    products: list[ProductUpdateBase]

    class Config:
        from_attributes = True

