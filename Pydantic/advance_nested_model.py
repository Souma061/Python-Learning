from pydantic import BaseModel
from typing import List, Optional, Union


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class Company(BaseModel):
    name:str
    address: Optional[Address] = None

class Employee(BaseModel):
    name: str
    age: int
    company: Optional[Company] = None



class TextContent(BaseModel):
    type:str = "text"
    content:str

class ImageContent(BaseModel):
    type:str = "image"
    url:str


class Article(BaseModel):
    sections: List[Union[TextContent, ImageContent]]
