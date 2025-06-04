from fastapi import FastAPI
from database import Base, engine
from api.client import router as client_router
from api.sale import router as sale_router
from api.product import router as product_router
from api.seller import router as seller_router
from fastapi.staticfiles import StaticFiles
from api.routes import endpoint

app = FastAPI()
app.mount("/public/static",StaticFiles(directory="./public/static"),name="static")



app.include_router(client_router, prefix="/client",
tags=["client"])
app.include_router(product_router, prefix="/product",
tags=["product"])
app.include_router(sale_router, prefix="/sale",
tags=["sale"])
app.include_router(seller_router, prefix="/seller",
tags=["seller"])

app.include_router(endpoint.router)


#agregar ruta para el gront

@app.get("/")
async def hola_mundo():
    return {"mensaje": "Hola mundo"}
