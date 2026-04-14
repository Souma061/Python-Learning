from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

DATABASE_URL = "sqlite:///./expenses.db"

engine = create_engine(DATABASE_URL,echo=False)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass

