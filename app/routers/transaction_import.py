from pymongo import MongoClient
import pandas as pd
import os
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from io import BytesIO
from models.transaction import Transaction
from bson import ObjectId 

# Get the absolute path of the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
router = APIRouter(prefix="/api/v1", tags=["Import File"])
client = MongoClient(host="mongodb+srv://phuchauxd12:Abcd0123@cluster0.lf8sh9p.mongodb.net/").get_database("dev")
db = client.get_collection("TRANSACTION_HISTORY")

@router.post('/transaction/{user_id}/import_csv')
def TransactionHistory(user_id: str,csv_file: UploadFile = File(...)):
    try:
        # Read the CSV file
        headers = ['transaction_name','transaction_date','Amount','acccount_id','user_id','transaction_type', 'tag_id']
        df = pd.read_csv(BytesIO(csv_file.file.read()), names=headers, skiprows= 1)
        data = df.to_dict(orient='records')
        for value in data:
            db.insert_one(
                Transaction(transaction_name= value['transaction_name'],   transaction_date= value["transaction_date"], Amount= value["Amount"],
                            transaction_type= value["transaction_type"], user_id= ObjectId(user_id)
                            ).dict()
            )
        return JSONResponse(content={"message": "Transaction created successfully"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
