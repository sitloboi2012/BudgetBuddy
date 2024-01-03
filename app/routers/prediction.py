from bson import ObjectId
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from sklearn.linear_model import LinearRegression
from constant import Constant, TRANSACTION_COLLECTION
import pandas as pd
from models.transaction import GetTransactionInformation
from pymongo import MongoClient
from skforecast.ForecasterAutoreg import ForecasterAutoreg


# Connect to DB
router = APIRouter(prefix="/api/v1", tags=["Income Prediction"])

#Get route of prediction
@router.get('/prediction/{user_id}')
def income_prediction(user_id:str):
    #Check to see if user ID exist
    list_transaction = TRANSACTION_COLLECTION.find({"user_id": ObjectId(user_id)})
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
            def datas():
                df = pd.DataFrame(array)
                headers = ['transaction_date', 'Amount']    
                df = df[headers]    
                df = df.groupby('transaction_date').sum().reset_index()
                df['transaction_date'] = pd.to_datetime(df['transaction_date'], dayfirst=True)
                df = df.set_index('transaction_date')
                df = df.sort_index()
                return df
            """ Past will fetch all the history transaction date of the user,
            combined, all the dates that has the same day, into one. We then use that data to make prediction
            for the upcoming 6 months."""
            
            
            df = datas()
            def loop():
                data_input = []
                data_input.append(df['Amount'].tolist())
                data_input = sum(data_input, [])
                forecast = ForecasterAutoreg(regressor=LinearRegression(), lags=2)
                
                """ The prediction work recursively as in, it will make a prediction for one day ahead, after that 
                we will append that prediction and used that new prediction for the next prediction. We will repeat 
                the steps as how much we want, in this case we did it recuresively for 180 which is equivalant to 6 months"""
                for time in range(1,d_future,1):
                    forecast.fit(y = pd.Series(data_input))
                    predictions = forecast.predict(steps = 1)
                    predictions = round(predictions, 0)
                    predictions = predictions.tolist()
                    data_input = data_input + predictions
                data_input = data_input[5:]    
                """ This removes the alread exited transaction history, and will only return the predicted transaction """
                return data_input
                
            return loop()
    #This will predicts for the next upcoming 3 months    
    return JSONResponse(content=recursive_prediction(90))