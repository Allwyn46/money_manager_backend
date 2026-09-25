import uuid
from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class TransactionBase(BaseModel):
    """Fields shared by all transaction schemas."""

    date: date
    category: str | None = None
    amount: Decimal | None = Field(default=None, gt=0)
    account: str | None = None
    note: str | None = None
    transaction_type: str | None = None
    from_account: str | None = None
    to_account: str | None = None


class TransactionCreate(TransactionBase):
    """Schema for creating a new transaction (no client-supplied ID)."""


class TransactionRead(TransactionBase):
    """Schema for returning a transaction, including its database ID."""

    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID