# -*- coding: utf-8 -*-
from __future__ import annotations

from pydantic import BaseModel, Field
from typing_extensions import Annotated
from pymongo import ReturnDocument
from bson import ObjectId


class UserInfo(BaseModel):
    """
    Object to describe User Information
    """

    username: str = Field(...)
    full_name: str = Field(...)
    password: str = Field(...)
