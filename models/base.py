from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass
