from database import engine
from db_models import ProductDB

Base = ProductDB.metadata
Base.create_all(bind=engine)
