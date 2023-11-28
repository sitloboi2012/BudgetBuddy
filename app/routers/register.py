# -*- coding: utf-8 -*-
from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from models.users import UserInfo
from constant import Constant
from pymongo import MongoClient

router = APIRouter(prefix="/api/v1", tags=["User Register"])
client = MongoClient(host=Constant.MONGODB_URI).get_database("dev")
db = client.get_collection("USERS")


@router.post("/register")
def register_user(
    user_name: str = Form(..., description="Username of the user"),
    password: str = Form(..., description="Password of the user"),
    full_name: str = Form(..., description="Full name of the user"),
):
    db.insert_one(
        UserInfo(username=user_name, full_name=full_name, password=password).dict()
    )
