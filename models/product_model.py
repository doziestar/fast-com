from models import Base


class ProductBase(Base):
    title: str
    price: float
    description: str
    tax: float
    category: list[str]
    image: str
    tags: list[str]


class CreateProductModel(ProductBase):
    pass


class ProductResponseModel(ProductBase):
    id: str
    created_at: str
    updated_at: str
