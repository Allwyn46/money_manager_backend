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


class CategoryBase(BaseModel):
    category_name: str


class CategoryRead(CategoryBase):
    
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID

class CategoryCreate(CategoryBase):
    """Schema for creating a new transaction (no client-supplied ID)."""


class AccountBase(BaseModel):
    account_name: str


class AccountRead(AccountBase):
    
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID

class AccountCreate(AccountBase):
    """Schema for creating a new transaction (no client-supplied ID)."""


class ExpenseBase(BaseModel):
    date: date
    category: str | None = None
    amount: Decimal | None = Field(default=None, gt=0)
    account: str | None = None
    note: str | None = None

class ExpenseRead(ExpenseBase):
    
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID

class ExpenseCreate(ExpenseBase):
    """Schema for creating a new transaction (no client-supplied ID)."""