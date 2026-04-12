from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    price: float
    description: str
    quantity: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

    # def __init__(self, id: int, name: str, price: float, description: str, quantity: int):
    #     self.id = id
    #     self.name = name
    #     self.price = price
    #     self.description = description
    #     self.quantity = quantity
