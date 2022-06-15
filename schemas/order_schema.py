from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from schemas import BaseSchema


class OrderSchema(BaseSchema):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("UserSchema", back_populates="orders")
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    product = relationship("ProductSchema", back_populates="orders")
