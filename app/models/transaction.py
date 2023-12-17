from pydantic import BaseModel, Field
from datetime import datetime
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator
PyObjectId = Annotated[str, BeforeValidator(str)]

class Transaction(BaseModel):
    transaction_name : str = Field(alias="transaction_name", default=None)
    transaction_date : datetime =Field(alias=" transaction_date", default=None)
    Amount : float = Field(alias="Amount", default=None)
    account_id: PyObjectId = Field(alias="account_id", default=None)
    user_id: PyObjectId = Field(alias="user_id", default=None)
    transaction_type: str = Field(alias="transaction_type", default=None)
    tag_id: PyObjectId = Field(alias="tap_id", default=None)