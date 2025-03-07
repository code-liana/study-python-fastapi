from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None  = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: Optional[bool] = False
    items: list[Item] = []

    class Config:
        from_attributes = True
