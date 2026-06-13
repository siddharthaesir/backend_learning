"""
the code below has,
database table mapping
ORM representation of DB rows

using SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String
from app.db import Base

class User(Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)