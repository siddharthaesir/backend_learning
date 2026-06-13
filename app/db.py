# create_engine is for creating the database cman (connection manager)
# postgres connection string syntax = postgresql://username:password@host:port/service_name
# sessionmaker, as the name suggests creates user session on the database
# declarative_base, for creating the parent class of the ORM models (here named Base)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/backend_learning"

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