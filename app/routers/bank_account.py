from __future__ import annotations

from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from constant import Constant
from pymongo import MongoClient
from models.bank_account import (
    SavingOrInvestmentAccount,
    ExpenseAccount,
    AccountGeneric,
)
from bson import ObjectId

router = APIRouter(prefix="/api/v1", tags=["CRUD Bank Account"])

# MONGODB CONNECTION
client = MongoClient(host=Constant.MONGODB_URI).get_database("dev")
bank_collection = client.get_collection("BANK_INFO")
account_collection = client.get_collection("ACCOUNTS")
saving_collection = client.get_collection("SAVING_ACCOUNTS")
investment_collection = client.get_collection("INVESTMENT_ACCOUNTS")
expense_collection = client.get_collection("EXPENSE_ACCOUNTS")

# MODEL INITIALIZATION
model = {
    "Saving": [SavingOrInvestmentAccount, saving_collection],
    "Investment": [SavingOrInvestmentAccount, investment_collection],
    "Expense": [ExpenseAccount, expense_collection],
}


def create_new_account_generic(user_id: str, bank_id: str, number_of_account: int = 1):
    account_generic = AccountGeneric(
        user_id=ObjectId(user_id), bank_id=ObjectId(bank_id), number_of_account=number_of_account
    ).dict()
    account_collection.insert_one(account_generic)
    return account_generic["_id"]


# create account manually
@router.post("/bank_account/{user_id}/create_manually")
def create_account_manually(
    user_id: str,
    account_name: str = Form(..., description="Account name of the bank account"),
    account_type: str = Form(..., description="Account type of the bank account"),
    current_balance: float = Form(
        ..., description="Current balance of the bank account"
    ),
    bank_name: str = Form(..., description="Bank name of the bank account"),
) -> JSONResponse:
    if account_type not in model:
        return JSONResponse(
            status_code=422, content={"message": "Invalid account type"}
        )

    if bank_collection.find_one({"bank_name": bank_name}) is None:
        return JSONResponse(status_code=422, content={"message": "Invalid bank name"})

    if (
        account_collection.find_one({"account_name": account_name, "user_id": user_id})
        is not None
    ):
        return JSONResponse(
            status_code=409, content={"message": "Account name already exists"}
        )

    account_model = model[account_type][0]
    bank_id = bank_collection.find_one({"bank_name": bank_name})["_id"]

    if (account_collection.find_one({"bank_id": bank_id, "user_id": user_id})) is None:
        account_id = create_new_account_generic(user_id=user_id, bank_id=bank_id)
    else:
        query = {"bank_id": account_name, "user_id": user_id}
        account_collection.update_one(query, {"$inc": {"number_of_account": 1}})
        account_id = account_collection.find_one(
            {"bank_id": account_name, "user_id": user_id}
        )["_id"]


    model[account_type][1].insert_one(
        account_model(
            account_name=account_name,
            account_id=ObjectId(account_id),
            user_id=ObjectId(user_id),
            bank_id=ObjectId(bank_id),
            goal_id=None,
            current_balance=current_balance,
        ).dict()
    )

    return JSONResponse(
        status_code=200, content={"message": "Bank account created successfully"}
    )
