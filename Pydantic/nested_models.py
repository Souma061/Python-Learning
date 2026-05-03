
# Nested Models in Pydantic
from pydantic import BaseModel
from typing import List,Optional



class Address(BaseModel):
    street:str
    city:str
    zip_code:str


class User(BaseModel):
    id:int
    name:str
    address: Address # Nested model

address_1 = Address(
    street="123 Main St",
    city="Anytown",
    zip_code="12345"
)
user_1 = User(
    id=1,
    name="John Doe",
    address=address_1
)


print(f"User ID: {user_1.id}, Name: {user_1.name}, Address: {user_1.address.street}, {user_1.address.city}, {user_1.address.zip_code}")


userData = {
    "id": 2,
    "name": "Jane Smith",
    "address": {
        "street": "456 Elm St",
        "city": "Othertown",
        "zip_code": "67890"
    }
}

user_2 = User(**userData)
print(f"User ID: {user_2.id}, Name: {user_2.name}, Address: {user_2.address.street}, {user_2.address.city}, {user_2.address.zip_code}")
