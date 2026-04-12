from sqlalchemy import Column, Integer, String, Float
from database import Base

class ProductDB(Base):
    __tablename__ = "products"


    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
