from abc import ABC, abstractmethod
from app.models.base import Product

class Creator(ABC):
    @abstractmethod
    def factory_method(self, **kwargs) -> Product:
        pass
