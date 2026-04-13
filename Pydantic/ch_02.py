from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True  # Default value for in_stock

Product1 = {
    "id": 101,
    "name": "Laptop",
    "price": 999.99
}

Product2 = {
    "id": 102,
    "name": "Smartphone",
    "price": 499.99,
    "in_stock": False
}
product =Product(**Product1)
print(f"Product ID: {product.id}, Name: {product.name}, Price: {product.price}, In Stock: {product.in_stock}")
product2 =Product(**Product2)
print("\n")
print(f"Product ID: {product2.id}, Name: {product2.name}, Price: {product2.price}, In Stock: {product2.in_stock}")
