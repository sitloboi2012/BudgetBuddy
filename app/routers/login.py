from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from models.users import UserInfo
from constant import Message, Constant
from pymongo import MongoClient
import bcrypt

router = APIRouter(prefix="/api/v1", tags=["User Register"])
client = MongoClient(host=Constant.MONGODB_URI).get_database("dev")
db = client.get_collection("USERS")

@router.post('/login', responses={401: {'model': Message}, 404: {'model': Message}})
def login(user_name: str = Form(..., description="Username of the user"),
          password: str = Form(..., description="Password of the user")):
    # Hash the input password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Find the user account in the database
    account = db.find_one({'username': user_name})
    
    if account:
        # Compare the hashed input password with the stored hashed password
        if bcrypt.checkpw(password.encode('utf-8'), account['password'].encode('utf-8')):
            return JSONResponse(content={"user_name": user_name, "password": hashed_password.decode('utf-8')})
        else:
            return JSONResponse(status_code=401, content={'message': "Password is incorrect."})
    else:
        return JSONResponse(status_code=404, content={'message': "User does not exist."})