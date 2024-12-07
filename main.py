from fastapi import FastAPI
from app.factories.product_factory import BiciCreator, MotoCreator
from app.registry.product_registry import ProductRegistry
from app.routes.product_routes import router

app = FastAPI()

# Registro de productos
ProductRegistry.register_creator("bici", BiciCreator())
ProductRegistry.register_creator("moto", MotoCreator())

# Registro de rutas
app.include_router(router, prefix="/products", tags=["Products"])
