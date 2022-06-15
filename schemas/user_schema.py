from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from schemas import BaseSchema


class UserSchema(BaseSchema):
    __tablename__ = "users"

    firstname = Column(String, nullable=False, default="")
    lastname = Column(String, nullable=False, default="")
    username = Column(String, nullable=False, default="")
    email = Column(String, nullable=False, default="")
    password = Column(String, nullable=False, default="")

    products = relationship("ProductSchema", back_populates="owner")
    orders = relationship("OrderSchema", back_populates="user")

    @property
    async def fullname(self):
        return f"{self.firstname} {self.lastname}"

    async def hashPassword(self, password):
        return password

    async def sendEmail(self, subject, body):
        return True
