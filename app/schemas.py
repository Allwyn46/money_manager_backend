from datetime import date
from decimal import Decimal
from pydantic import BaseModel, Field


class Transaction(BaseModel):

    date: date
    category: str = Field(..., min_length=1)
    amount: Decimal = Field(..., gt=0, description="Transaction amount, must be positive")
    account: str = Field(..., min_length=1)
    note: str = ""

