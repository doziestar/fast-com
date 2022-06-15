from models import Base


class CartModel(Base):
    id: int
    user_id: int
    products: list[dict]
    total_price: float
    created_at: str
    updated_at: str


class CreateCart(Base):
    user_id: int
    products: list[dict]
