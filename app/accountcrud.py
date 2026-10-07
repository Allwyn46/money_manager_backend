from app.schemas import AccountCreate
import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Account

async def add_account(
    db:AsyncSession, account: AccountCreate
)-> Account:
    db_account = Account(**account.model_dump())
    db.add(db_account)
    await db.commit()     
    await db.refresh(db_account)
    return db_account

async def get_account(
    db: AsyncSession, account_id: uuid.UUID
) -> Account | None:
    result = await db.execute(
        select(Account).where(Account.id == account_id)
    )
    return result.scalar_one_or_none()


async def get_accounts(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> list[Account]:
    result = await db.execute(
        select(Account)
        .order_by(Account.created_at.desc())
        .offset(skip)
        .limit(limit)
    )
    return list(result.scalars().all())