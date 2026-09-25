import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Transaction
from app.schemas import TransactionCreate


async def create_transaction(
    db: AsyncSession, transaction: TransactionCreate
) -> Transaction:
    db_transaction = Transaction(**transaction.model_dump())
    db.add(db_transaction)
    await db.commit()
    await db.refresh(db_transaction)
    return db_transaction


async def get_transaction(
    db: AsyncSession, transaction_id: uuid.UUID
) -> Transaction | None:
    result = await db.execute(
        select(Transaction).where(Transaction.id == transaction_id)
    )
    return result.scalar_one_or_none()


async def get_transactions(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> list[Transaction]:
    result = await db.execute(
        select(Transaction)
        .order_by(Transaction.date.desc())
        .offset(skip)
        .limit(limit)
    )
    return list(result.scalars().all())