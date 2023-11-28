# -*- coding: utf-8 -*-
from enum import StrEnum
from pydantic import BaseModel

import os


class Constant(StrEnum):
    MONGODB_URI = os.environ["MONGODB_URI"]


class Message(BaseModel):
    message: str
