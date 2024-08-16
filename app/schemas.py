# app/schemas.py
from pydantic import BaseModel, constr, conint
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    id: constr(min_length=1, max_length=50)
    gender: constr(max_length=1)
    birth_year: Optional[conint(gt=1900, lt=2100)]  # 출생 년도 1900~2100 사이


class UserCreate(UserBase):
    password: constr(min_length=6)


class User(UserBase):
    id: str
    gender: str
    birth_year: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
