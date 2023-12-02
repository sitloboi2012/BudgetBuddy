# -*- coding: utf-8 -*-
from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from models.users import UserInfo
from models.router_response import Message
# from constant import Constant
from pymongo import MongoClient
import bcrypt


router = APIRouter(prefix="/api/v1", tags=["User Register"])
client = MongoClient(host="mongodb+srv://phuchauxd12:Abcd0123@cluster0.lf8sh9p.mongodb.net/").get_database("dev")
db = client.get_collection("USERS")


@router.post("/register", responses= {409: {"model": Message},
                                      422: {"model": Message}})
def register_user(
    user_name: str = Form(..., description="Username of the user"),
    password: str = Form(..., description="Password of the user"),
    full_name: str = Form(..., description="Full name of the user"),
    number: str = Form(None, description="Phone number of the user"),
    email: str = Form(..., description="Email address of the user"),
    address: str = Form(None, description="Address of the user")
):
    password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    if db.find_one({'username': user_name}):
        return JSONResponse(status_code=409, content={"message": "Username already exists"})
    if db.find_one({'email': email}):
        return JSONResponse(status_code=409, content={"message": "Email already exists"})
    try: 
        db.insert_one(
            UserInfo(username=user_name, full_name=full_name, password=password, number=number, email= email, address= address).dict())
    except ValueError as e:
        # Handle Pydantic validation errors
        return JSONResponse(status_code=422, content={"message": str(e)}) # error for email and number
    
    assert db.find_one({'username': user_name})['username'] == user_name # test case 
    assert len(list(db.find({'username': user_name}))) == 1    # test case

    return JSONResponse(content={"user_name": user_name, "password": password.decode('utf-8'), "full_name": full_name, "number": number, "email": email, "address": address})

