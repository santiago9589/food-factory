from fastapi import FastAPI
from database import Base, engine
from api.client import router as client_router
from api.sale import router as sale_router
from api.product import router as product_router
from api.seller import router as seller_router

app = FastAPI()

app.include_router(client_router, prefix="/client",
tags=["client"])
app.include_router(product_router, prefix="/product",
tags=["product"])
app.include_router(sale_router, prefix="/sale",
tags=["sale"])
app.include_router(seller_router, prefix="/seller",
tags=["seller"])





@app.get("/")
async def hola_mundo():
    return {"mensaje": "Hola mundo"}
