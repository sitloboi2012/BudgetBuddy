from __future__ import annotations

from models.transaction import GetTransactionInformation

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from constant import Message, Constant
from pymongo import MongoClient
from bson import ObjectId
import re

router = APIRouter(prefix="/api/v1", tags=["Report Data Page"])
client = MongoClient(host= Constant.MONGODB_URI ).get_database("dev")
TRANSACTION_COLLECTION = client.get_collection("TRANSACTION_HISTORY")

@router.get("/report/{user_id}/{month}/{year}")
def get_monthly_transaction_data(
    user_id: str,
    month: str,
    year: str
):
    regx = re.compile(f"^{year}-{month}", re.IGNORECASE)
    transaction = TRANSACTION_COLLECTION.find({"user_id": ObjectId(user_id), "transaction_date": {"$regex": regx}})
    return JSONResponse(status_code=status.HTTP_200_OK, content=[GetTransactionInformation(**transaction).dict() for transaction in transaction])