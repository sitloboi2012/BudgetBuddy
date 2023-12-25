# -*- coding: utf-8 -*-
from __future__ import annotations

from pydantic import BaseModel, Field
from bson import ObjectId


class GoalSettingBaseModel(BaseModel):
    goal_created_date: str = Field(..., description="Goal created date")
    goal_end_date: str = Field(..., description="Goal end date")
    goal_name: str = Field(..., description="Goal name")
    account_id: ObjectId = Field(..., description="Account id")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class InvestmentGoalModel(BaseModel):
    goal_id: ObjectId = Field(..., description="Goal id")
    investment_account_id: ObjectId = Field(..., description="Investment account id")
    current_profit: float = Field(..., description="Current profit")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class SavingGoalModel(BaseModel):
    goal_id: ObjectId = Field(..., description="Goal id")
    saving_account_id: ObjectId = Field(..., description="Saving account id")
    saving_goal_value: float = Field(..., description="Saving goal value")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
