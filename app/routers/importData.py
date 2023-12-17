from pymongo import MongoClient
import pandas as pd
import os
# from constant import Constant

# Get the absolute path of the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

client = MongoClient(host="mongodb+srv://phuchauxd12:Abcd0123@cluster0.lf8sh9p.mongodb.net/").get_database("dev")
db = client.get_collection("empHisTranDB")

headers = ['Transaction Name','Transaction Date','Amount','Description','Account Name','Original Balance','Remain Balance']

# Create a DB if not exist


# Function that fetch information from FE
"""
Fetch information from the FE
There are going to be 2 types of file import
Transaction 
"""
import_as = input('Import Transaction or Bank information: ')
if import_as == 'IT':
    transaction = client.get_collection("TransactionHistory")
    headers1 = ['Transaction Name','Transaction Date','Amount','Description','Account Name','Original Balance','Remain Balance']
    transac_path = os.path.join(current_directory, 'SampleBankAccount-BudgetBuddy-HistoricalTransaction.csv')
    transac = pd.read_csv(transac_path, names=headers1)
    data1 = transac.to_dict(orient='records')
    print(transaction.insert_many(data1))
else:
    bankinfo = client.get_collection("AccountInfo")
    headers2 = ['Account','Account Type','Current Balance','Saving Time','Interest Rate']
    account_path = os.path.join(current_directory, 'SampleBankAccount-BudgetBuddy-BankInformation.csv')
    account = pd.read_csv(account_path, names=headers2)
    data2 = account.to_dict(orient='records')
    print(bankinfo.insert_many(data2))