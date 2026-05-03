from pydantic import BaseModel
from typing import Dict,List,Optional

class Cart(BaseModel):
    id:int
    items: List[str]
    quantities: Dict[str,int]



class BlogPost(BaseModel):
    title:str
    content:str
    imagUrl: Optional[str] = None  # Optional field with default value None


cart_1 = Cart(
    id=1,
    items=["Laptop", "Mouse", "Keyboard"],
    quantities={"Laptop": 1, "Mouse": 2, "Keyboard": 1}
)

print(f"Cart ID: {cart_1.id}, Items: {cart_1.items}, Quantities: {cart_1.quantities}")


blogPost_1 = BlogPost(
    title="My First Blog Post",
    content="This is the content of my first blog post.",
    # imageUrl="https://example.com/image.jpg"
)

print(f"Blog Post Title: {blogPost_1.title}, Content: {blogPost_1.content}, Image URL: {blogPost_1.imagUrl}")
