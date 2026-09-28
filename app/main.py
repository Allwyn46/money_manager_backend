import uuid
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud
from app import categorycrud
from app.database import Base, engine, get_db
from app.schemas import TransactionCreate, TransactionRead, CategoryRead, CategoryCreate


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Create database tables on startup."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="Money Manager API", lifespan=lifespan)


@app.get("/")
async def root() -> dict[str, str]:
    """Return a simple greeting to confirm the API is running."""
    return {"message": "Hello World"}


@app.get("/transactions", response_model=list[TransactionRead])
async def list_transactions(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
) -> list[TransactionRead]:
    """List transactions, paginated and ordered by most recent date."""
    return await crud.get_transactions(db, skip=skip, limit=limit)


@app.get("/transactions/{transaction_id}", response_model=TransactionRead)
async def get_transaction(
    transaction_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
) -> TransactionRead:
    """Return a single transaction by ID, or 404 if it doesn't exist."""
    transaction = await crud.get_transaction(db, transaction_id)
    if transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found"
        )
    return transaction


@app.post(
    "/transactions",
    response_model=TransactionRead,
    status_code=status.HTTP_201_CREATED,
)
async def add_transaction(
    transaction: TransactionCreate,
    db: AsyncSession = Depends(get_db),
) -> TransactionRead:
    """Create a new transaction."""
    return await crud.create_transaction(db, transaction)


""" CATEGORY ROUTES """

@app.post(
    "/category",
    response_model=CategoryRead,
    status_code=status.HTTP_201_CREATED,
)
async def add_category(
    category: CategoryCreate,
    db: AsyncSession = Depends(get_db),
)->CategoryRead:
    return await categorycrud.create_category(db, category)