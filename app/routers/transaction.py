from pymongo import MongoClient
import pandas as pd
import os
from fastapi import APIRouter, File, UploadFile, Form
from fastapi.responses import JSONResponse
from io import BytesIO
from models.transaction import Transaction, GetTransactionInformation
from bson import ObjectId 
from datetime import datetime
from constant import Constant

# Get the absolute path of the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
router = APIRouter(prefix="/api/v1", tags=["Import Transaction"])
client = MongoClient(host=Constant.MONGODB_URI).get_database("dev")
db = client.get_collection("TRANSACTION_HISTORY")
BANK_COLLECTION = client.get_collection("BANK_INFO")
ACCOUNT_COLLECTION = client.get_collection("ACCOUNTS")



@router.post('/transaction/{user_id}/import_csv')
def post_transaction(user_id: str,csv_file: UploadFile = File(...)):
    try:
        # Read the CSV file
        headers = ['transaction_name','Payee','transaction_date','Amount','bank_name','transaction_type']
        df = pd.read_csv(BytesIO(csv_file.file.read()), names=headers, skiprows= 1)
        data = df.to_dict(orient='records')

        for value in data:

            # Check if the bank exist
            bank = BANK_COLLECTION.find_one({"bank_name": value["bank_name"]})
            if bank is None:
                return JSONResponse(status_code=422, content={ "message": f"Invalid bank name: {value}"})
            bank_id = bank["_id"]

            # Check if account exist
            account = ACCOUNT_COLLECTION.find_one({"user_id": ObjectId(user_id), "bank_id": ObjectId(bank_id)})
            if account is None:
                return JSONResponse(status_code=404, content={'message': "Account does not exist."})
            account_id = account["_id"]

            # Check if the transaction already exist 
            existing_transaction = db.find_one({
                "transaction_name": value['transaction_name'],
                "Payee": value['Payee'],
               "transaction_date":datetime.strptime(value["transaction_date"], "%d/%m/%Y").strftime("%d-%b-%Y"),
                "Amount": value["Amount"],
                "bank_name": value["bank_name"],
                "account_id": ObjectId(account_id),
                "transaction_type": value["transaction_type"],
                "user_id": ObjectId(user_id)
            })
            if existing_transaction is not None:
                return JSONResponse(status_code=409, content={"message": "Transaction already exists"})
            db.insert_one(
                Transaction(transaction_name= value['transaction_name'],Payee= value['Payee'], transaction_date= value["transaction_date"], Amount= value["Amount"],
                            bank_name= value["bank_name"],account_id=ObjectId(account_id), transaction_type= value["transaction_type"], user_id= ObjectId(user_id)
                            ).dict()
            )
        return JSONResponse(content={"message": "Transaction created successfully"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@router.get("/transaction/{user_id}")
def get_transaction(user_id: str):
    list_transaction = db.find({"user_id": ObjectId(user_id)})
    array = [
           GetTransactionInformation(
                transaction_id = str(value["_id"]),
                transaction_name=value["transaction_name"],
                transaction_date=value["transaction_date"],
                Payee=value["Payee"],
                Amount=value["Amount"],
                bank_name=value["bank_name"],
                transaction_type=value["transaction_type"],
            ).dict()
            for value in list_transaction
        ]

    if not array:
        return JSONResponse(status_code=404, content={'message': "Transaction does not exist."})
        
    return JSONResponse(content=array)


@router.put("/transaction/{user_id}/{transaction_id}/update")
def update_transaction(
    user_id: str,
    transaction_id: str,
    transaction_name: str = Form(..., description="Name of the transaction"),
    Payee: str = Form(..., description="Payee of the transaction"),
    transaction_date: str = Form(..., description="Date of the transaction (format: %d/%m/%Y)"),
    Amount: float = Form(..., description="Amount of the transaction"),
    bank_name: str = Form(..., description="Name of the bank"),
    transaction_type: str = Form(..., description="Type of the transaction"),
):
    try:
        # Check if the bank exist
        bank = BANK_COLLECTION.find_one({"bank_name": bank_name})
        if bank is None:
            return JSONResponse(status_code=422, content={ "message": f"Invalid bank name: {bank_name}"})
        bank_id = bank["_id"]

        # Check if account exist
        account = ACCOUNT_COLLECTION.find_one({"user_id": ObjectId(user_id), "bank_id": ObjectId(bank_id)})
        if account is None:
            return JSONResponse(status_code=404, content={'message': "Account does not exist."})
        account_id = account["_id"]
    
        # Update the transaction
        db.update_one(
            {"_id": ObjectId(transaction_id), "user_id": ObjectId(user_id)},
            {
                "$set": {
                    "transaction_name": transaction_name,
                    "Payee": Payee,
                    "transaction_date": datetime.strptime(transaction_date, "%d/%m/%Y").strftime("%d-%b-%Y"),
                    "Amount": Amount,
                    "bank_name": bank_name,
                    "transaction_type": transaction_type,
                    "account_id": account_id
                }
            }
        )
        return JSONResponse(content={"message": "Transaction updated successfully"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)})



@router.delete("/transaction/{user_id}/{transaction_id}/delete")
def delete_transaction(user_id: str, transaction_id: str):
    try:
        # Delete the transaction
        db.find_one_and_delete({"_id": ObjectId(transaction_id), "user_id": ObjectId(user_id)})

        return JSONResponse(content={"message": "Transaction deleted successfully"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

