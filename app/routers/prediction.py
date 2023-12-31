from bson import ObjectId
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from sklearn.ensemble import RandomForestRegressor
from constant import Constant
import pandas as pd
from models.transaction import GetTransactionInformation
from pymongo import MongoClient
from skforecast.ForecasterAutoreg import ForecasterAutoreg


# Connect to DB
router = APIRouter(prefix="/api/v1", tags=["Income Prediction"])
client = MongoClient(host=Constant.MONGODB_URI).get_database("dev")
db = client.get_collection("TRANSACTION_HISTORY")

#Get route of prediction
@router.get('/prediction/{user_id}')
def income_prediction(user_id:str):
    #Check to see if user ID exist
    list_transaction = db.find({"user_id": ObjectId(user_id)})
    array = [
           GetTransactionInformation(
                transaction_id = str(value["_id"]),
                transaction_name=value["transaction_name"],
                transaction_date=value["transaction_date"],
                Payee=value["Payee"],
                Amount=value["Amount"],
                account_name=value["account_name"],
                account_type=value["account_type"],
                transaction_type=value["transaction_type"],
            ).dict()
            for value in list_transaction
        ]
    if not array:
        return JSONResponse(status_code=404, content={'message': "Transaction does not exist."})
    
    #Fetch history transaction to predict 
    def recursive_prediction(d_future):
            df = pd.DataFrame(array)
            headers = ['transaction_date', 'Amount']    
            df = df[headers]
            df['transaction_date'] = pd.to_datetime(df['transaction_date'], dayfirst=True)
            past =(len(df['transaction_date'].unique())-1)
            """ Past will fetch all the history transaction date of the user,
            combined, all the dates that has the same day, into one. We then use that data to make prediction
            for the upcoming 6 months."""
            prediction = ForecasterAutoreg(regressor = RandomForestRegressor(), lags = past)
            prediction.fit(y = df['Amount'])
            forecasting = jsonable_encoder(prediction.predict(steps=d_future).to_dict())
            return forecasting
        
    #Predict the next 6 months of income = 180 days.
    return JSONResponse(content=recursive_prediction(180))
