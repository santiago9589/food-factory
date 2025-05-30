from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from . import schemas, models 
from ..seller.models import Seller
from .. client.models import Client
from fastapi import HTTPException
from ..product.models import Product
from ..sale.models import SellProduct,Sale
from ..sale.schemas import SaleResponse,SaleBase
from ..product.schemas import ProductUpdateBase
async def create_sale(db: AsyncSession, sale: SaleBase):

    # Verificar vendedor
     #TODO METODO PARA VERIFICAR
    result_seller = await db.execute(select(Seller).filter(Seller.id == sale.seller))
    seller = result_seller.scalar_one_or_none()
    if not seller:
        raise HTTPException(status_code=404, detail="Vendedor no encontrado")

    # Verificar cliente
    #TODO METODO PARA VERIFICAR
    result_client = await db.execute(select(Client).filter(Client.id == sale.client))
    client = result_client.scalar_one_or_none()
    if not client:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    # Crear venta
    #TODO METODO PARA CREAR LA SALE
    new_sale = Sale(
        dateofBuy=sale.dateofBuy,
        total=sale.total,
        seller_id=seller.id,
        client_id=client.id
    )
    db.add(new_sale)
    await db.flush()  # Consigue el ID

    product_responses = []

    for product_data in sale.products:
        result = await db.execute(select(Product).filter(Product.id == product_data.id))
        product = result.scalar_one_or_none()

        if not product:
            raise HTTPException(status_code=404, detail=f"Producto con ID {product_data.id} no encontrado")

        if product.quantity < product_data.quantity:
            raise HTTPException(status_code=400, detail=f"Stock insuficiente para producto {product.id}")

        db_sell_product = SellProduct(
            sale_id=new_sale.id,
            product_id=product.id,
            quantity=product_data.quantity
        )
        db.add(db_sell_product)

        product.quantity -= product_data.quantity

        # Armar respuesta por producto
        #TODO METODO PARA CREAR LISTA
        product_responses.append(
            ProductUpdateBase(
                id=product.id,
                product_name=product.product_name,
                description=product.description,
                quantity=product_data.quantity
            )
        )

    await db.commit()
    await db.refresh(new_sale)

    # Devolver respuesta en formato SaleResponse
    return SaleResponse(
        sale_id=new_sale.id,
        dateofBuy=new_sale.dateofBuy,
        total=new_sale.total,
        seller=new_sale.seller_id,
        client=new_sale.client_id,
        products=product_responses
    )
    