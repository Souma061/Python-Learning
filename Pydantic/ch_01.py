
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id:int
    name: str
    is_active: bool


input_data = {
    "id": "123",
    "name": "John Doe",
    "is_active": False
}

user = User(**input_data)
print(f"User ID: {user.id}, Name: {user.name}, Active: {user.is_active}")



# For use pydantic validation error handling we need to use Basemodel and try except block to catch the validation error and print the error message.

# Import Basemodel
# Tyoe annotation for the input data
# Model init(Always unpack the input data using **)
# Catch the validation error using try except block and print the error message.
# auto validation of the data types and values based on the defined model.
