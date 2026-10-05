from app.schemas import AccountCreate
import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Account

async def add_account(
    db:AsyncSession, account, AccountCreate
)-> Account:
    db_account = Account(**account.model_dump())
    db.add(db_account)
    await db.refresh(db_account)
    return db_account