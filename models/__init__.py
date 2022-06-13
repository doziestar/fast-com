from pydantic import BaseModel


class Base(BaseModel):
    id: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True
