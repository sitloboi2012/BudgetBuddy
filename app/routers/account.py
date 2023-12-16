# -*- coding: utf-8 -*-
from fastapi import APIRouter, Form, Body
from fastapi.responses import JSONResponse
from models.bank_account import BankAccountInformation, AllBankAccount
from constant import Constant
from pymongo import MongoClient


router = APIRouter(prefix="/api/v1", tags=["Account Creation"])
client = MongoClient(host=Constant.MONGODB_URI).get_database("dev")
db = client.get_collection("ACCOUNTS")


@router.post(
    "/create_bank_account/{user_id}",
    response_description="Create bank account for user",
    response_model=BankAccountInformation,
    response_model_by_alias=False,
)
def create_bank_account(
    user_id: str,
    bank_id: str = Form(..., description="Bank id of the bank"),
    number_of_account: int = Form(..., description="Number of account of the user"),
):
    return db.insert_one(
        BankAccountInformation(
            user_id=user_id, bank_id=bank_id, number_of_account=number_of_account
        ).dict()
    )


@router.get(
    "/get_bank_account/{user_id}",
    response_description="Get all bank account of a user",
    response_model=AllBankAccount,
    response_model_by_alias=False,
)
def get_bank_account_info(user_id: str):
    return AllBankAccount(list_of_bank_account=list(db.find({"user_id": user_id})))


@router.put(
    "/update_bank_account/{user_id}",
    response_description="Update bank account of a user",
    response_model=BankAccountInformation,
    response_model_by_alias=False,
)
def update_bank_account_info(user_id: str, update_info_type: str, new_info: str):
    pass


@router.delete(
    "/delete_bank_account/{user_id}",
    response_description="Delete bank account of a user",
    response_model=BankAccountInformation,
    response_model_by_alias=False,
)
def delete_bank_account_info(user_id: str):
    pass
