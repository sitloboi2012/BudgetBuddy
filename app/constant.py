# -*- coding: utf-8 -*-
#from enum import StrEnum
from pydantic import BaseModel
from enum import Enum


import os
from dotenv import load_dotenv
import os

class StrEnum(str, Enum):
    pass

# Load environment variables from the local.env file
load_dotenv(os.path.join(os.path.dirname(__file__), "local.env"))

class Constant(StrEnum):
    MONGODB_URI =  'mongodb+srv://phuchauxd12:Abcd0123@cluster0.lf8sh9p.mongodb.net/'



class Message(BaseModel):
    message: str
