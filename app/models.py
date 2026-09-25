import uuid
from datetime import date as py_date
from decimal import Decimal

from sqlalchemy import Date, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    date: Mapped[py_date] = mapped_column(Date)
    category: Mapped[str | None] = mapped_column(String(255))
    amount: Mapped[Decimal | None] = mapped_column(Numeric(12, 2))
    account: Mapped[str | None] = mapped_column(String(255))
    note: Mapped[str | None] = mapped_column(String(255))
    transaction_type: Mapped[str | None] = mapped_column(String(255))
    from_account: Mapped[str | None] = mapped_column(String(255), nullable=True)
    to_account: Mapped[str | None] = mapped_column(String(255), nullable=True)