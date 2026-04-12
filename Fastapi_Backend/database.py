import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


load_dotenv(Path(__file__).resolve().parent / ".env")

DATABASE_URL = URL.create(
	drivername=os.getenv("DB_DRIVER", "mysql+pymysql"),
	username=os.getenv("DB_USER", "souma"),
	password=os.getenv("DB_PASSWORD", ""),
	host=os.getenv("DB_HOST", "127.0.0.1"),
	port=int(os.getenv("DB_PORT", "3306")),
	database=os.getenv("DB_NAME", "fastapi_db"),
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
