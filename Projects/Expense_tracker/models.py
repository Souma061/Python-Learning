from sqlalchemy import Column, Integer, String, Float, Date, Enum
from datetime import date
from database import Base
import enum


class Category(enum.Enum):
    food = "Food"
    transportation = "Transportation"
    entertainment = "Entertainment"
    utilities = "Utilities"
    other = "Other"

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    amount = Column(Float, nullable=False)
    notes = Column(String, nullable=True)
    date = Column(Date, default=date.today)
    category = Column(Enum(Category), nullable=False)


    def __repr__(self) -> str:
        return f"Expense(id={self.id}, amount={self.amount}, notes='{self.notes}', date={self.date}, category='{self.category.value}')"
