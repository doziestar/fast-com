from typing import ClassVar

from config import db
from sqlalchemy import Column, DateTime, String
from utils.uuid import generate_uuid, get_current_date_time


class BaseSchema(db.SQL_Base):
    __abstract__: ClassVar[bool] = True
    id = Column(String, primary_key=True, nullable=False, unique=True, index=True, default=generate_uuid)
    created_at = Column(DateTime, nullable=False, default=get_current_date_time)
    updated_at = Column(DateTime, nullable=False, default=get_current_date_time)
