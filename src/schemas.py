from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict


class GroupModel(BaseModel):
    name: str = Field(max_length=50)


class GroupResponse(GroupModel):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ContactBase(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    surname: str = Field(min_length=2, max_length=150)
    email: str = Field(min_length=5, max_length=150)
    phone_number: str = Field(min_length=3, max_length=20)
    birthday: date = Field(default=None)


class ContactModel(ContactBase):
    groups: List[int]


class ContactUpdate(ContactModel):
    is_active: bool


class ContactIsActiveUpdate(BaseModel):
    is_active: bool


class ContactResponse(ContactModel):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] | None
    is_active: bool
    address_id: Optional[int]
    groups: List[GroupResponse] | None

    model_config = ConfigDict(from_attributes=True)
