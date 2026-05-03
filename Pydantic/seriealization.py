from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street:str
    city:str
    zip_code:str

class User(BaseModel):
    id:int
    name:str
    email:str
    address: Address
    created_at: datetime
    tags:List[str]

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )



user = User(
    id=1,
    name="John Doe",
    email="john.doe@example.com",
    address=Address(
        street="123 Main St",
        city="Anytown",
        zip_code="12345",
    ),
    created_at=datetime(2024, 11, 18, 12, 0, 0),
    tags=["python", "pydantic"]
)
print(user.model_dump_json())
print(user.model_dump_json(indent=4))
print(user.model_dump())
