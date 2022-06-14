from pydantic import BaseModel

from models import Base


class UserBase(BaseModel):
    email: str
    username: str
    firstname: str
    lastname: str


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class User(UserBase):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        validate_assignment = True
