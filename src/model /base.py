import logging

from uuid import uuid4

from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base

logger = logging

class BaseModel(Base):
    """Base model for all models"""
    __abstract__ = True

    id: Mapped[str] = mapped_column(
        primary_key=True,
        unique=True,
        default=uuid4,
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        onupdate=func.now(),
    )
