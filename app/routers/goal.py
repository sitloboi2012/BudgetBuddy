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
GOAL_SETTING_BASE = client.get_collection("GOAL_SETTINGS")


@router.post("/goal_saving_setting/{user_id}")
def set_goal(
    user_id: str,
    goal_end_date: str = Form(..., description="Goal end date"),
    goal_created_date: str = Form(..., description="Goal created date"),
    goal_name: str = Form(..., description="Goal name"),
    connected_account_id: Optional[str] = Form(None, description="Account id"),
    connected_account_name: Optional[str] = Form(None, description="Account name"),
    goal_value: float = Form(..., description="Goal value"),
    
) -> JSONResponse:
    
    if GOAL_SETTING_BASE.find_one({"user_id": ObjectId(user_id), "goal_name": goal_name}):
        raise HTTPException(status_code=400, detail="Goal name already exists")
    
    start_date = datetime.strptime(goal_created_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(goal_end_date, "%Y-%m-%d").date()

    if start_date < datetime.now().date():
        raise HTTPException(status_code=400, detail="Start date cannot be in the past")

    if end_date < start_date:
        raise HTTPException(
            status_code=400, detail="End date must be greater than start date"
        )

    if connected_account_id is None:
        GOAL_SETTING_BASE.insert_one(
            GoalSettingBaseModel(
                user_id=ObjectId(user_id),
                goal_created_date=goal_created_date,
                goal_end_date = goal_end_date,
                goal_name=goal_name,
                saving_amount=goal_value,
                connected_account_name = None,
                connected_account_id = None
            ).dict()
        )
    else:
        GOAL_SETTING_BASE.insert_one(
            GoalSettingBaseModel(
                user_id=ObjectId(user_id),
                goal_created_date=goal_created_date,
                goal_end_date = goal_end_date,
                goal_name=goal_name,
                saving_amount=goal_value,
                connected_account_id=ObjectId(connected_account_name),
                connected_account_name=connected_account_name
            ).dict()
        )
    
    return JSONResponse(
        status_code=200,
        content = "Create Goal Saving Success"
    )

@router.get("/goal_saving_setting/{user_id}/{goal_id}")
def get_single_goal_view(
    user_id: str,
    goal_id: str,
):
    goal = GOAL_SETTING_BASE.find_one({"_id": ObjectId(goal_id), "user_id": ObjectId(user_id)})
    if goal is None:
        raise HTTPException(status_code=400, detail="Goal not found")
    return JSONResponse(
        status_code=200,
        content=GoalModelView(**goal).dict()
    )

@router.get("/goal_saving_setting/{user_id}")
def get_all_goal_view(
    user_id: str,
):
    goals = GOAL_SETTING_BASE.find({"user_id": ObjectId(user_id)})
    return JSONResponse(
        status_code=200,
        content=[GoalModelView(**goal).dict() for goal in goals]
    )

@router.put("/goal_saving_setting/{user_id}/{goal_id}/update")
def update_goal(
    user_id: str,
    goal_id: str,
    goal_end_date: str = Form(None, description="Goal end date"),
    goal_created_date: str = Form(None, description="Goal created date"),
    goal_name: str = Form(None, description="Goal name"),
    connected_account_id: Optional[str] = Form(None, description="Account id"),
    connected_account_name: Optional[str] = Form(None, description="Account name"),
    goal_value: float = Form(None, description="Goal value"),
) -> JSONResponse:
    goal = GOAL_SETTING_BASE.find_one({"_id": ObjectId(goal_id), "user_id": ObjectId(user_id)})
    if goal is None:
        raise HTTPException(status_code=400, detail="Goal not found")
    
    if goal_end_date is not None:
        end_date = datetime.strptime(goal_end_date, "%Y-%m-%d").date()
        if end_date < datetime.now().date():
            raise HTTPException(status_code=400, detail="End date cannot be in the past")
        goal["goal_end_date"] = goal_end_date

    if goal_created_date is not None:
        start_date = datetime.strptime(goal_created_date, "%Y-%m-%d").date()
        if start_date < datetime.now().date():
            raise HTTPException(status_code=400, detail="Start date cannot be in the past")
        goal["goal_created_date"] = goal_created_date

    if goal_name is not None:
        goal["goal_name"] = goal_name

    if goal_value is not None:
        goal["saving_amount"] = goal_value

    if connected_account_id is not None:
        goal["connected_account_id"] = ObjectId(connected_account_id)
        goal["connected_account_name"] = connected_account_name

    GOAL_SETTING_BASE.update_one({"_id": ObjectId(goal_id)}, {"$set": goal})
    return JSONResponse(
        status_code=200,
        content = "Update Goal Saving Success"
    )

@router.delete("/goal_saving_setting/{user_id}/{goal_id}/delete")
def delete_goal(
    user_id: str,
    goal_id: str,
) -> JSONResponse:
    goal = GOAL_SETTING_BASE.find_one({"_id": ObjectId(goal_id), "user_id": ObjectId(user_id)})
    if goal is None:
        raise HTTPException(status_code=400, detail="Goal not found")
    GOAL_SETTING_BASE.delete_one({"_id": ObjectId(goal_id)})
    return JSONResponse(
        status_code=200,
        content = "Delete Goal Saving Success"
    )