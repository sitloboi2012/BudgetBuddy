from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator
from bson import ObjectId
class Transaction(BaseModel):
    transaction_name : str = Field(alias="transaction_name", default=None)
    transaction_date : str = Field(...,alias="transaction_date")
    Payee : str = Field(alias="Payee", default=None)
    Amount : float = Field(...,alias="Amount")
    bank_name : str = Field(...,alias="bank_name")
    account_id: ObjectId = Field(alias="account_id", default=None)
    user_id: ObjectId = Field(alias="user_id", default=None)
    transaction_type: str = Field(alias="transaction_type", default=None)

    
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

class GetTransactionInformation(BaseModel):
    transaction_id: str = Field(alias="transaction_id", default=None)
    transaction_name : str = Field(alias="transaction_name", default=None)
    transaction_date : str = Field(...,alias="transaction_date")
    Payee : str = Field(alias="Payee", default=None)
    Amount : float = Field(...,alias="Amount")
    bank_name : str = Field(...,alias="bank_name")
    transaction_type: str = Field(alias="transaction_type", default=None)
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed=True
        json_encoders = {
            ObjectId: str
        }

