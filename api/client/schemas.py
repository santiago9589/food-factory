from pydantic import BaseModel
from typing import Optional
from datetime import date
from sqlalchemy import String, Integer, Column, Date, Boolean, ForeignKey, Float

class Person:
    name = Column(String(11))
    lastname = Column(String(11))
    dateofbirth = Column(Date)


class ClientBase(BaseModel):
    name:str
    lastname:str
    dateofbirth:date
    address: str

    class Config:
        orm_mode = True