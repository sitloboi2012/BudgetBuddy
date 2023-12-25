# -*- coding: utf-8 -*-
from __future__ import annotations

from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import JSONResponse
from constant import Constant
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from typing import Optional
from models.goal import GoalSettingBaseModel, GoalModelView

router = APIRouter(prefix="/api/v1", tags=["Goal Setting"])
client = MongoClient(host=Constant.MONGODB_URI).get_database("dev")
SAVING_GOAL_DB = client.get_collection("SAVING_GOAL_SETTINGS")
INVESTMENT_GOAL_DB = client.get_collection("INVESTMENT_GOAL_SETTINGS")
GOAL_SETTING_BASE = client.get_collection("GOAL_SETTINGS")


@router.post("/goal_saving_setting/{user_id}")
def set_goal(
    goal_end_date: str = Form(..., description="Goal end date"),
    goal_created_date: str = Form(..., description="Goal created date"),
    goal_name: str = Form(..., description="Goal name"),
    connected_account_name: Optional[str] = Form(..., description="Account id"),
    goal_value: float = Form(..., description="Goal value"),
) -> JSONResponse:
    
    
    start_date = datetime.strptime(goal_created_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(goal_end_date, "%Y-%m-%d").date()

    if start_date < datetime.now().date():
        raise HTTPException(status_code=400, detail="Start date cannot be in the past")

    if end_date < start_date:
        raise HTTPException(
            status_code=400, detail="End date must be greater than start date"
        )

    if connected_account_name is None:
        GOAL_SETTING_BASE.insert_one(
            GoalSettingBaseModel(
                goal_created_date=goal_created_date,
                goal_end_date = goal_end_date,
                goal_name=goal_name,
                saving_amount=goal_value,
            ).dict()
        )
    else:
        GOAL_SETTING_BASE.insert_one(
            GoalSettingBaseModel(
                goal_created_date=goal_created_date,
                goal_end_date = goal_end_date,
                goal_name=goal_name,
                saving_amount=goal_value,
                connected_account=ObjectId(connected_account_name),
            ).dict()
        )
    
    return JSONResponse(
        status_code=200,
        content = "Create Goal Saving Success"
    )

