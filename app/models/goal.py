# -*- coding: utf-8 -*-
from __future__ import annotations

from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId


class GoalSettingBaseModel(BaseModel):
    goal_created_date: datetime.date = Field(..., description="Goal created date")
    goal_end_date: datetime.date = Field(..., description="Goal end date")
    goal_name: str = Field(..., description="Goal name")


class InvestmentGoalModel(GoalSettingBaseModel):
    goal_id: ObjectId = Field(..., description="Goal id")
    investment_account_id: ObjectId = Field(..., description="Investment account id")
    current_profit: float = Field(..., description="Current profit")


class SavingGoalModel(GoalSettingBaseModel):
    goal_id: ObjectId = Field(..., description="Goal id")
    saving_account_id: ObjectId = Field(..., description="Saving account id")
    saving_goal_value: float = Field(..., description="Saving goal value")
