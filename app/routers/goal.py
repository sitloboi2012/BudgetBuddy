# -*- coding: utf-8 -*-
from __future__ import annotations

from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import JSONResponse
from constant import Constant
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from models.goal import InvestmentGoalModel, SavingGoalModel, GoalSettingBaseModel

router = APIRouter(prefix="/api/v1", tags=["Goal Setting"])
client = MongoClient(host=Constant.MONGODB_URI).get_database("dev")
SAVING_GOAL_DB = client.get_collection("SAVING_GOAL_SETTINGS")
INVESTMENT_GOAL_DB = client.get_collection("INVESTMENT_GOAL_SETTINGS")
GOAL_SETTING_BASE = client.get_collection("GOAL_SETTINGS")

# MODEL INITIALIZATION
MODEL = {
    "Saving": [SavingGoalModel, SAVING_GOAL_DB],
    "Investment": [InvestmentGoalModel, INVESTMENT_GOAL_DB],
}


@router.post("/goal_setting/{user_id}/{account_id}")
def set_goal(
    account_id: str,
    account_type: str = Form(..., description="Account type"),
    goal_end_date: str = Form(..., description="Goal end date"),
    goal_created_date: str = Form(..., description="Goal created date"),
    goal_name: str = Form(..., description="Goal name"),
) -> JSONResponse:
    start_date = datetime.strptime(goal_created_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(goal_end_date, "%Y-%m-%d").date()

    if start_date < datetime.now().date():
        raise HTTPException(status_code=400, detail="Start date cannot be in the past")

    if end_date < start_date:
        raise HTTPException(
            status_code=400, detail="End date must be greater than start date"
        )

    GOAL_SETTING_BASE.insert_one(
        GoalSettingBaseModel(
            goal_created_date=goal_created_date,
            goal_end_date=goal_end_date,
            goal_name=goal_name,
            account_id=ObjectId(account_id),
        ).dict()
    )

    goal_id = GOAL_SETTING_BASE.find_one(
        {"goal_name": goal_name, "account_id": ObjectId(account_id)}
    )["_id"]

    print(goal_id)
    """
    if account_type == "Saving":
        SAVING_GOAL_DB.insert_one(
            SavingGoalModel(
                goal_id=ObjectId(account_id),
                saving_account_id=ObjectId(account_id),
                saving_goal_value=0,
            ).dict()
        )
    """
