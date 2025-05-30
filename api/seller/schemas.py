from pydantic import BaseModel
from typing import Optional
from datetime import date


class SellerBase(BaseModel):
    name:str
    lastname:str
    dateofbirth:date
    is_online: bool

    class Config:
        orm_mode = True