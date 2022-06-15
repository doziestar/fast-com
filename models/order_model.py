from models import Base


class OrderBase(Base):
    id: int
    user_id: int
    product_id: int
    quantity: int
    price: float
    created_at: str
    updated_at: str


class CreateOrder(Base):
    user_id: int
    product_id: int
    quantity: int
    price: float
