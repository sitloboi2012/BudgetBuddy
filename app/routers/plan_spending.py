from __future__ import annotations

from fastapi import APIRouter, HTTPException, Form
from fastapi.responses import JSONResponse
from bson import ObjectId
from constant import PLANNING_SPENDING_COLLECTION, EXPENSE_SPENDING_COLLECTION, TRANSACTION_COLLECTION
from datetime import datetime

from models.plan_spending import PlannedSpendingModel, PlannedSpendingModelView, MonthlyExpensePlan, MonthlyExpensePlanModelView, TransactionModelView

router = APIRouter(prefix="/api/v1", tags=["Plan Settings"])

@router.post("/plan_spending/{user_id}/create")
def create_spending(
    user_id: str,
    spending_name: str = Form(..., description="Name of the spending"),
    amount: int | float = Form(..., description="Amount of the spending"),
    spending_type: str = Form(..., description="Type of the spending. This should either be Income, Bills, Subscription or Credit Card Payment"),
    time_duration: str = Form(..., description="Time duration of the spending planning. Example: Jan 2024, Feb 2024, etc.")
):
    if PLANNING_SPENDING_COLLECTION.find_one({"user_id": ObjectId(user_id), "spending_name": spending_name, "time_duration":time_duration}) is not None:
        raise HTTPException(status_code=400, detail="Spending name already exist")
    
    spending = PlannedSpendingModel(
        spending_name=spending_name,
        amount=amount,
        user_id=ObjectId(user_id),
        spending_type=spending_type,
        time_duration=time_duration
    ).dict()
    PLANNING_SPENDING_COLLECTION.insert_one(spending)
    return JSONResponse(status_code=200, content={"message": "Spending created successfully"})

@router.get("/plan_spending/{user_id}/{timeframe}")
def get_all_spending(user_id: str, timeframe: str):
    spendings = PLANNING_SPENDING_COLLECTION.find({"user_id": ObjectId(user_id), "time_duration": timeframe})
    list_speding = []
    for spending in spendings:
        spending_dict = PlannedSpendingModelView(**spending).dict()
        spending_dict["id"] = str(spending["_id"])
        list_speding.append(spending_dict) 
    return JSONResponse(status_code=200,content= list_speding)

@router.put("/plan_spending/{user_id}/{spending_id}")
def update_spending(
    user_id: str,
    spending_id: str,
    spending_name: str = Form(..., description="Name of the spending"),
    amount: int | float = Form(..., description="Amount of the spending"),
    spending_type: str = Form(..., description="Type of the spending. This should either be Income, Bills, Subscription or Credit Card Payment"),
    time_duration: str = Form(..., description="Time duration of the spending planning. Example: Jan 2024, Feb 2024, etc.")
):
    spending = PLANNING_SPENDING_COLLECTION.find_one({"_id": ObjectId(spending_id)})
    if spending is None:
        raise HTTPException(status_code=400, detail="Spending does not exist")
    
    PLANNING_SPENDING_COLLECTION.update_one(
        {"_id": ObjectId(spending_id)},
        {"$set": {
            "spending_name": spending_name,
            "amount": amount,
            "spending_type": spending_type,
            "time_duration": time_duration
        }}
    )
    return JSONResponse(status_code=200, content={"message": "Spending updated successfully"})

@router.delete("/plan_spending/{user_id}/{spending_id}")
def delete_spending(user_id: str, spending_id: str):
    spending = PLANNING_SPENDING_COLLECTION.find_one({"_id": ObjectId(spending_id)})
    if spending is None:
        raise HTTPException(status_code=400, detail="Spending does not exist")
    
    PLANNING_SPENDING_COLLECTION.delete_one({"_id": ObjectId(spending_id), })
    return JSONResponse(status_code=200, content={"message": "Spending deleted successfully"})


@router.post("/monthly_expense_plan/{user_id}/create")
def create_monthly_expense_plan(
    user_id: str,
    category: str = Form(..., description="Category of the spending"),
    initial_amount: int | float = Form(..., description="Initial amount of the spending"),
    time_duration: str = Form(..., description="Time Duration for Expense Planning. For example: Jan 2024, Feb 2023, etc.")
):
    if EXPENSE_SPENDING_COLLECTION.find_one({"user_id": ObjectId(user_id), "category": category ,"time_duration":time_duration}) is not None:
        raise HTTPException(status_code=400, detail="Spending name already exist")
    
    spending = MonthlyExpensePlan(
        user_id=ObjectId(user_id),
        category=category,
        initial_amount=initial_amount,
        current_total_use=0,
        time_duration = time_duration
    ).dict()
    EXPENSE_SPENDING_COLLECTION.insert_one(spending)
    return JSONResponse(status_code=200, content={"message": "Spending created successfully"})

@router.get("/monthly_expense_plan/{user_id}")
def get_all_monthly_expense_plan(user_id: str):
    spendings = EXPENSE_SPENDING_COLLECTION.find({"user_id": ObjectId(user_id)})
    list_speding = []
    for spending in spendings:
        spending_dict = MonthlyExpensePlanModelView(**spending).dict()
        spending_dict["id"] = str(spending["_id"])
        parsed_date = datetime.strptime(spending["time_duration"], "%b %Y")
        formatted_date = parsed_date.strftime("%Y-%m")
        list_transaction = TRANSACTION_COLLECTION.find({"user_id": ObjectId(user_id), "category": spending["category"]})
        list_transaction_by_date = [TransactionModelView(**transaction).dict() for transaction in list_transaction if formatted_date in transaction["transaction_date"]]
        spending_dict["list_transaction"] = list_transaction_by_date
        list_speding.append(spending_dict) 
    return JSONResponse(
        status_code=200,
        content= list_speding)
    
@router.delete("/monthly_expense_plan/{user_id}/{spending_id}")
def delete_monthly_expense_plan(user_id: str, spending_id: str):
    spending = EXPENSE_SPENDING_COLLECTION.find_one({"_id": ObjectId(spending_id)})
    if spending is None:
        raise HTTPException(status_code=400, detail="Spending does not exist")
    
    EXPENSE_SPENDING_COLLECTION.delete_one({"_id": ObjectId(spending_id), })
    return JSONResponse(status_code=200, content={"message": "Spending deleted successfully"})