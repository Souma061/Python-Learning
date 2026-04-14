
from sqlalchemy import func
from database import Session, engine
from models import Expense, Category, Base
from datetime import date
from typing import Optional

def init_db():
    Base.metadata.create_all(engine)


def add_expense(amount: float,notes: str, category: str = "other")-> Expense:
    with Session() as session:
        expense = Expense(
            amount = amount,
            notes = notes,
            category = Category[category],
            date = date.today()
        )
        session.add(expense)
        session.commit()
        session.refresh(expense)
        return expense


def list_expenses(month: Optional[int] = None, year: Optional[int] = None) -> list[Expense]:
    with Session() as session:
        query = session.query(Expense)
        if month and year:
            query = query.filter(func.extract('month', Expense.date) == month, func.extract('year', Expense.date) == year)
        elif month:
            query = query.filter(func.extract('month', Expense.date) == month)
        elif year:
            query = query.filter(func.extract('year', Expense.date) == year)
        return query.all()


def delete_expenses(expense_id: int) -> bool:
    with Session() as session:
        expense = session.query(Expense).filter(Expense.id == expense_id).first()
        if expense:
            session.delete(expense)
            session.commit()
            return True
        return False



def monthly_summary(month:int, year:int) -> dict[str, float]:
    with Session() as session:
        summary = session.query(Expense.category, func.sum(Expense.amount)).filter(
            func.extract('month', Expense.date) == month,
            func.extract('year', Expense.date) == year
        ).group_by(Expense.category).all()
        return {category.name: total for category, total in summary}


def sort_by_category(expenses: list[Expense]) -> dict[str, list[Expense]]:
    sorted_expenses = {}
    for expense in expenses:
        category = expense.category.value
        if category not in sorted_expenses:
            sorted_expenses[category] = []
        sorted_expenses[category].append(expense)
    return sorted_expenses


