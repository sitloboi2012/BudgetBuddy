# -*- coding: utf-8 -*-
from pymongo import MongoClient

from constant import Constant


def main():
    CLIENT = MongoClient(host=Constant.MONGODB_URI)
    DB = CLIENT.get_database("BudgetBuddy-DB")
    if DB:
        print("Hello World")


if __name__ == "__main__":
    main()
