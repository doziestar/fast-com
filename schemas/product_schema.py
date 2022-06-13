from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from schemas import BaseSchema


class ProductSchema(BaseSchema):
    __tablename__ = "products"

    tax = Column(Float, nullable=False, default=10)
    price = Column(Float, nullable=False, default=0)
    title = Column(String, nullable=False, default="")
    description = Column(Text, nullable=False, default="")
    active = Column(Boolean, nullable=False, default=True)
    quantity = Column(Integer, nullable=False, default=0)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("UserSchema", back_populates="products")

    @property
    async def calculate_tax(self):
        return self.price * self.tax / 100

    @property
    async def decrease_quantity(self, quantity):
        self.quantity -= quantity
        return self.quantity
