from pydantic import BaseModel, field_validator,model_validator
from datetime import datetime

class Person(BaseModel):
    name:str
    surname:str

    @field_validator('name', 'surname')
    def validate_names(cls, value):
        if not value.isalpha():
            raise ValueError("Names must contain only alphabetic characters")
        return value
user = Person(name="John", surname="Doe")
print(f"Name: {user.name}, Surname: {user.surname}")

# user2 = Person(name="John123", surname="Doe")


class User(BaseModel):
    email:str


    @field_validator('email')
    def normalize_email(cls, value):
        return value.lower()


class Product(BaseModel):
    price: str

    @field_validator('price',mode='before')
    def validate_price(cls, value):
        if isinstance(value, str):
            value = value.replace('$', '').replace(',','')  # Remove dollar sign if present
            try:
                return float(value)
            except ValueError:
                raise ValueError("Price must be a valid number")
        return value


class Daterange(BaseModel):
    start_date: datetime
    end_date: datetime


    @model_validator(mode='after')
    def validate_date_range(cls, values):
        if values.end_date < values.start_date:
            raise ValueError("End date must be after start date")
        return values
