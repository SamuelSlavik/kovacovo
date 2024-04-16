from typing import Optional
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    id: int
    email: str
    password: str

    class Config:
        from_attributes = True


class CreateUser(BaseModel):
    email: str
    password: str
