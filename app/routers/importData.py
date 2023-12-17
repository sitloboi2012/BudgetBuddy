from pymongo import MongoClient
import pandas as pd
import os
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from io import BytesIO
from models.transaction import Transaction

# Get the absolute path of the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
router = APIRouter(prefix="/api/v1", tags=["Import File"])
client = MongoClient(host="mongodb+srv://phuchauxd12:Abcd0123@cluster0.lf8sh9p.mongodb.net/").get_database("dev")
db = client.get_collection("TransactionHistory")

@router.post('/transaction')
def TransactionHistory(csv_file: UploadFile = File(...)):
    try:
        # Read the CSV file
        headers1 = ['transaction_name','transaction_date','Amount','acccount_id','user_id','transaction_type', 'tag_id']
        df = pd.read_csv(BytesIO(csv_file.file.read()), names=headers1, skiprows= 1)
        data = df.to_dict(orient='records')
        for value in data:
            db.insert_one(
                Transaction(transaction_name= value['transaction_name'],  transaction_date= value['transaction_date'], Amount= value["Amount"],
                            transaction_type= value["transaction_type"]
                            ).dict()
            )
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
# """
# Fetch information from the FE
# There are going to be 2 types of file import
# Transaction 
# """
# import_as = input('Import Transaction or Bank information: ')
# if import_as == 'IT':
#     transaction = client.get_collection("TransactionHistory")
#     headers1 = ['Transaction Name','Transaction Date','Amount','acccount_id','user_id','transaction_type', 'tag_id']
#     transac_path = os.path.join(current_directory, 'SampleBankAccount-BudgetBuddy-HistoricalTransaction.csv')
#     transac = pd.read_csv(transac_path, names=headers1)
#     print( transac)
#     data1 = transac.to_dict(orient='records')
#     # print(transaction.insert_many(data1))
#     print(data1)
# else:
#     bankinfo = client.get_collection("AccountInfo")
#     headers2 = ['Account','Account Type','Current Balance','Saving Time','Interest Rate']
#     account_path = os.path.join(current_directory, 'SampleBankAccount-BudgetBuddy-BankInformation.csv')
#     account = pd.read_csv(account_path, names=headers2)
#     data2 = account.to_dict(orient='records')
#     # print(bankinfo.insert_many(data2))
#     print(data2)