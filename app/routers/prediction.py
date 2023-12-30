import warnings
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
warnings.filterwarnings('ignore')


router = APIRouter(prefix="/api/v1", tags=["Income Prediction"])
client = MongoClient(host=Constant.MONGODB_URI).get_database("dev")
db = client.get_collection("TRANSACTION_HISTORY")

@router.get('/prediction/{user_id}')
def income_prediction(past: int, future: int, user_id):
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
    """ This takes the user ID, as every user has their own ID and 
    transaction. By inputting a user id, it filters out the transaction history
    and only display the transaction to its users."""
    
    def recursive_prediction(d_past, d_future ):
        df = pd.DataFrame(array)
        headers = ['transaction_date', 'Amount']
        df = df[headers]
        df['transaction_date'] = pd.to_datetime(df['transaction_date'], dayfirst=True)
        prediction = ForecasterAutoreg(regressor = RandomForestRegressor(), lags = d_past)
        prediction.fit(y = df['Amount'])
        forecasting = jsonable_encoder(prediction.predict(steps=d_future).to_dict())
        return forecasting
    
    return recursive_prediction(past, future)
