from pydantic import BaseModel,field_validator,model_validator



class User(BaseModel):
    username:str
    email:str
    password:str

    @field_validator('password')
    def validate_password(cls, value):
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters long")
        return value


user_1 = User(
    username="john_doe",
    email="user@gmail.com",
    password="soumabrata"
)
print(f"Username: {user_1.username}, Email: {user_1.email}, Password: {user_1.password}")


class Signup(BaseModel):
    name:str
    email:str
    password:str
    confirm_password:str
    phone_number:str

    @model_validator(mode='after') # the mode="After" is deprecated in pydantic v2.0, we need to use the model_validator decorator with the mode="after" to validate the confirm_password field after the model is initialized.

    # model validator is used to validate the model after it is initialized, we can use it to validate the confirm_password field after the model is initialized.
    def validate_phone_number(self):
        if not self.phone_number.isdigit() or len(self.phone_number) != 10:
            raise ValueError("Phone number must be a 10-digit number")
        return self

user_2 = Signup(
    name="John Doe",
    email="john.doe@gmail.com",
    password="password123",
    confirm_password="password123",
    phone_number="1234567890"

)

print(f"Name: {user_2.name}, Email: {user_2.email}, Password: {user_2.password}, Confirm Password: {user_2.confirm_password}, Phone Number: {user_2.phone_number}")
