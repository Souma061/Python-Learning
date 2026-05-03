from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True  # Default value for in_stock

product_1 = Product(
    id=1,
    name="Laptop",
    price=999.99,
    in_stock=False
)

print(f"Product ID: {product_1.id}, Name: {product_1.name}, Price: {product_1.price}, In Stock: {product_1.in_stock}")
