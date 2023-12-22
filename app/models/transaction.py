from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator
from bson import ObjectId
class Transaction(BaseModel):
    transaction_name : str = Field(alias="transaction_name", default=None)
    transaction_date : datetime.date = Field(...,alias="transaction_date")
    Amount : float = Field(...,alias="Amount")
    account_id: ObjectId = Field(alias="account_id", default=None)
    user_id: ObjectId = Field(alias="user_id", default=None)
    transaction_type: str = Field(alias="transaction_type", default=None)
    tag_id: ObjectId = Field(alias="tap_id", default=None)

    @validator("Amount", pre=True, allow_reuse=True)
    def parse_amount(cls, value):
        return float(value.replace(".", ""))
    
    @validator("transaction_date", pre=True, allow_reuse=True)
    def date(cls, value):
        input_date = datetime.strptime(value, "%d/%m/%Y").date()
        formatted_date = input_date.strftime("%d-%b-%Y")
        return formatted_date
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed=True
        json_encoders = {
            ObjectId: str
        }
