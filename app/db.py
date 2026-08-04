# create_engine is for creating the database cman (connection manager)
# postgres connection string syntax = postgresql://username:password@host:port/service_name
# sessionmaker, as the name suggests creates user session on the database
# declarative_base, for creating the parent class of the ORM models (here named Base)
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


load_dotenv()           # reads local .env file into environment variables when the app starts

DATABASE_URL = os.getenv("DATABASE_URL")        # os.getenv() retrieves the URL w/o hardcoding it in source.
engine = create_engine(DATABASE_URL)

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set. Add it to the local .env file.")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# creating db session per request and safely closing it 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()