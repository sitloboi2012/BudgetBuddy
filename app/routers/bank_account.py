from __future__ import annotations

from fastapi import APIRouter, Form
from constant import Constant
from pymongo import MongoClient

router = APIRouter(prefix="/api/v1", tags=["CRUD Bank Account"])
client = MongoClient(host= Constant.MONGODB_URI ).get_database("dev")



# create account manually
@router.post("/bank_account/{user_id}/create_manually")
def create_account_manually(
    account_name: str =  Form(..., description="Account name of the bank account"),
    account_type: str = Form(..., description="Account type of the bank account"),
    current_balance: str = Form(..., description="Current balance of the bank account"),
    **kwargs
) :
    return {"message": "Bank account created successfully"}