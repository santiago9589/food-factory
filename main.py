from fastapi import FastAPI
from database import Base, engine
from routers import Client,Product,Sales,Seller



app = FastAPI()

app.include_router(Client.router, prefix="/client",
tags=["client"])
app.include_router(Product.router, prefix="/product",
tags=["product"])
app.include_router(Sales.router, prefix="/sale",
tags=["sale"])
app.include_router(Seller.router, prefix="/seller",
tags=["seller"])





@app.get("/")
async def hola_mundo():
    return {"mensaje": "Hola mundo"}
