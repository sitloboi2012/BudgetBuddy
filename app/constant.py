# -*- coding: utf-8 -*-
from enum import Enum
from pydantic import BaseModel

import os


class Constant(Enum):
    MONGODB_URI = os.environ["MONGODB_URI"]


class Message(BaseModel):
    message: str
