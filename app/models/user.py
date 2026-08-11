"""
the code below has,
database table mapping
ORM representation of DB rows

using SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String
from app.db import Base

# defining class & also when executed, SQLAlechemy's ORM machinery register this table information in Base, so now Base.metadata contains the table structure
# And this is what Alembic will also read.
class User(Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String(20), nullable=True)