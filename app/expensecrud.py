from app.schemas import ExpenseCreate
import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Expense,Transaction

async def add_expense(
    db: AsyncSession,
    expense: ExpenseCreate,
    transaction_type:str = "expense"
):
    db_expense = Expense(**expense.model_dump())
    transaction = Transaction(
        date=expense.date,
        category=expense.category,
        amount=expense.amount,
        account=expense.account,
        note=expense.note,
        transaction_type=transaction_type,
    )
    db.add_all([db_expense,transaction])
    await db.commit()
    await db.refresh(db_expense)
    await db.refresh(transaction)
    return db_expense
