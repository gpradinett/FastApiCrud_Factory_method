from fastapi import APIRouter, HTTPException
from app.registry.product_registry import ProductRegistry

router = APIRouter()

@router.post("/create/")
def create_product(product_type: str, payload: dict):
    creator = ProductRegistry.get_creator(product_type)
    if not creator:
        raise HTTPException(status_code=400, detail="Tipo de producto no soportado")

    product = creator.factory_method(**payload)
    return {"message": "Producto creado", "product": product.to_dict()}
