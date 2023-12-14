import pymongo
from pymongo import MongoClient
import pandas as pd

mongoClient = MongoClient('mongodb+srv://userDB:InC2QuunWeQUFOCm@userdb.opquo83.mongodb.net/')

# mongoClient = pymongo.MongoClient()
db = mongoClient['userDB']
collection = db['empHisTranDB'] 

headers = ['Transaction Name','Transaction Date','Amount','Description','Account Name','Original Balance','Remain Balance']

#Create a DB if not exist
db = mongoClient['UserBankInformation']

#Function that fetch information FE
""" 
Fetch information from the FE
There are going to be 2 types of file import
Transaction 
"""
import_as = input('Import Transaction or Bank information: ')
if import_as == 'IT':
    transaction = mongoClient['TransactionHistory']
    headers1 = ['Transaction Name','Transaction Date','Amount','Description','Account Name','Original Balance','Remain Balance']
    transac = pd.read_csv('Sample Bank Account - BudgetBuddy - Historical Transaction.csv', names = headers1)
    data1 = transac.to_dict(orient='records')
    print(db.transaction.insert_many(data1))
else:
    bankinfo = mongoClient['BankInfo']
    headers2 = ['Account','Account Type','Current Balance','Saving Time','Interest Rate']
    account = pd.read_csv('bankacc.csv', names = headers2)
    data2 = account.to_dict(orient='records')
    print(db.bankinfo.insert_many(data2))



