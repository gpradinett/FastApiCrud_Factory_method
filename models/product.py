from app.models.base import Product

class BiciProduct(Product):
    def __init__(self, color: str, caracteristica: str):
        self.color = color
        self.caracteristica = caracteristica

    def operation(self) -> str:
        return "Bicicleta creada"

    def to_dict(self) -> dict:
        return {"type": "bici", "color": self.color, "caracteristica": self.caracteristica}


class MotoProduct(Product):
    def __init__(self, potencia: str):
        self.potencia = potencia

    def operation(self) -> str:
        return "Moto creada"

    def to_dict(self) -> dict:
        return {"type": "moto", "potencia": self.potencia}
