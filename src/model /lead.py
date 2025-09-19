from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column
from src.leads.model import BaseModel


class Lead(BaseModel):
    __tablename__ = "leads"

    # Salesforce ID
    external_id: Mapped[str] = mapped_column(
        String,
        nullable=True,
    )

    first_name: Mapped[str] = mapped_column(
        String,
        nullable=True,
    )

    last_name: Mapped[str] = mapped_column(
        String,
        nullable=True,
    )

    email: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    phone: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    lead_source: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    __table_args__ = (
        Index('idx_created_at_status', 'status', 'created_at'),
    )