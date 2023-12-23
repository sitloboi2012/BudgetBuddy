# -*- coding: utf-8 -*-
from __future__ import annotations

from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import JSONResponse
from constant import Message, Constant
from pymongo import MongoClient
from bson import ObjectId

router = APIRouter(prefix="/api/v1", tags=["Goal Setting"])
client = MongoClient(host=Constant.MONGODB_URI).get_database("dev")
saving_goal_db = client.get_collection("SAVING_GOAL_SETTINGS")
investment_goal_db = client.get_collection("INVESTMENT_GOAL_SETTINGS")
goal_overall_db = client.get_collection("GOAL_OVERALL_SETTINGS")


@router.post("/goal_setting/{user_id}/{account_id}")
def set_goal(
    user_id: ObjectId,
    account_id: ObjectId,
    goal_end_date: str = Form(..., description="Goal end date"),
    goal_name: str = Form(..., description="Goal name"),
):
    pass
