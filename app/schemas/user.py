"""
This code below is the API contract:

structure
validation
parsing of incoming/outgoing data

using Pydantic.
"""

from pydantic import BaseModel

class UserCreate(BaseModel):
    id: int
    name: str
    email: str
    phone: str | None = None

class UserUpdate(BaseModel):
    name: str
    email: str
    phone: str | None = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str | None = None

    class Config:
        from_attributes = True

