from app.factories.base_factory import Creator

class ProductRegistry:
    _creators = {}

    @classmethod
    def register_creator(cls, name: str, creator: Creator):
        cls._creators[name] = creator

    @classmethod
    def get_creator(cls, name: str) -> Creator:
        return cls._creators.get(name)
