# -*- coding: utf-8 -*-
#from enum import StrEnum
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from the local.env file
load_dotenv(os.path.join(os.path.dirname(__file__), "local.env"))

class Constant():
    MONGODB_URI = os.environ["MONGODB_URI"]


class Message(BaseModel):
    message: str

client = MongoClient(host=Constant.MONGODB_URI).get_database("dev")
BANK_COLLECTION = client.get_collection("BANK_INFO")
ACCOUNT_COLLECTION = client.get_collection("ACCOUNTS")
SAVING_COLLECTION = client.get_collection("SAVING_ACCOUNTS")
INVESTMENT_COLLECTION = client.get_collection("INVESTMENT_ACCOUNTS")
EXPENSE_COLLECTION = client.get_collection("EXPENSE_ACCOUNTS")