from app.schemas import CategoryCreate
import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Transaction, Category
from app.schemas import TransactionCreate


async def create_category(
    db: AsyncSession, category: CategoryCreate
) -> Category:
    db_category = Category(**category.model_dump())
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category


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