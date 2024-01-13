from fastapi import APIRouter, HTTPException, Form, BackgroundTasks
from fastapi.responses import JSONResponse
from models.users import UserInfo
from constant import Message, USERS
from bson import ObjectId 
import bcrypt
import uuid
from fastapi.encoders import jsonable_encoder
from models.email import EmailSchema, send_email  


router = APIRouter(prefix="/api/v1", tags=["User Profile"])

@router.get("/profile/{id}", responses= {404: {"model": Message},
                                        422: {"model": Message},
                                        401:{'model': Message}})
def profile(id: str):
    """
    Return the user data information
    """
    if len(id) ==24:
        account = USERS.find_one({"_id": ObjectId(id)})
        if account:
            try:
                # Convert ObjectId to string
                account["_id"] = str(account["_id"])
                return account
            except ValueError as e:
                return JSONResponse(status_code=402, content={"message": str(e)})
        else:
            return JSONResponse(status_code=404, content={"message": "User not found"})
    else:
        return  JSONResponse(status_code=401, content={"message": "Unauthorized"})


@router.put("/profile_update/{id}")
def update_profile( id:str,
            background_tasks: BackgroundTasks,
            password_verify: str = Form(...),
            new_password: str = Form(None, description="Password of the user"),
            number: str = Form(None, description="Phone number of the user"),
            address: str = Form(None, description="Address of the user"),):
    """
    Send the update data, it can be password, number, address
    """
    update = {}

    account = USERS.find_one({"_id": ObjectId(id)})
    if account and bcrypt.checkpw(password_verify.encode('utf-8'), account['password'].encode('utf-8')):
            try:
                if number is not None:
                    update["number"] = number
                if address is not None:
                    update["address"] = address
                if new_password is not None:
                    NewKey = uuid.uuid1().hex
                    NewPassword = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                    update["password"] = NewPassword.decode('utf-8')
                    update["key"] = NewKey
                # Store the hashed password in the database
                newAccount = USERS.find_one_and_update(
                    {"_id": ObjectId(id)},
                    {"$set": update},
                    return_document=True  # Return the updated document
                )

                # Convert ObjectId to string before returning the JSON response
                newAccount["_id"] = str(account["_id"])
                if new_password is not None:
                    # Email send to the customer about the key for login
                    subject = "key for account login in Budget Buddy application"
                    body = "KEY: " + str(NewKey)
                    data = EmailSchema(to=newAccount["email"], subject=subject, body=body).dict()
                    background_tasks.add_task(send_email, data["to"], data["subject"], data["body"])

                return JSONResponse(content=jsonable_encoder(newAccount))
            except ValueError as e:
                return JSONResponse(status_code=422, content={"message": str(e)})
    else:

            return JSONResponse(status_code=404, content={"message": "User not found or password is incorrect"})

          
   

