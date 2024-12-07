from app.factories.base_factory import Creator
from app.models.product import BiciProduct, MotoProduct

class BiciCreator(Creator):
    def factory_method(self, color: str, caracteristica: str) -> BiciProduct:
        return BiciProduct(color=color, caracteristica=caracteristica)


class MotoCreator(Creator):
    def factory_method(self, potencia: str) -> MotoProduct:
        return MotoProduct(potencia=potencia)
