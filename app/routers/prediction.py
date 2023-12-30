import warnings
from fastapi import APIRouter
from pymongo import MongoClient
from constant import Constant
import pandas as pd
from sklearn.linear_model import LinearRegression
from pymongo import MongoClient
from skforecast.ForecasterAutoreg import ForecasterAutoreg
warnings.filterwarnings('ignore')


router = APIRouter(prefix="/api/v1", tags=["Income Prediction"])
client = MongoClient(host=Constant.MONGODB_URI).get_database("dev")
db = client.get_collection("TRANSACTION_HISTORY")

@router.get('/get_prediction')
def income_prediction(past: int, future: int):
    all_df = db.find()
    def recursive_prediction(d_past, d_future ):
        df = pd.DataFrame(all_df)
        headers = ['transaction_date', 'amount']
        df = df[headers]
        df['date'] = pd.to_datetime(df['date'], dayfirst=True)
        
        """This combined all data values that has the same dates into one
        Which means that, there will be no duplicated days for the same month"""
        
        df = df.groupby('date').sum().reset_index().set_index('date')
        future = d_future 
        past = d_past
        prediction = ForecasterAutoreg(regressor = LinearRegression(), lags = past)
        prediction.fit(y = df['total_income'])
        forecasting = prediction.predict(steps=future)
        return (forecasting)
    return (recursive_prediction(past, future))


