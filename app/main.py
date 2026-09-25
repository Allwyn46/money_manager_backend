from app.schemas import Transaction
from fastapi import FastAPI,HTTPException
import uuid

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}

@app.post("/transactions/expense")
async def add_expense()->Transaction:
    try:
        pass
    except Exception as e:
        raise HTTPException(status_code=400,detail="Couldn't add transactions")

    finally:
        pass