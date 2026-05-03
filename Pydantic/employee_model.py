from typing import Optional
from pydantic import BaseModel,Field

class Employee(BaseModel):
    id:int
    name:str = Field(..., min_length=3, max_length=50,description="Employee name must be between 3 and 50 characters")
    department: Optional[str] = 'General'  # Optional field with default value 'General'
    salary: float = Field(..., ge=10000, description="Salary must be greater than or equal to 10000")
