# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field, ConfigDict
from pydantic.functional_validators import BeforeValidator

from typing import Optional
from typing_extensions import Annotated
from bson import ObjectId

PyObjectId = Annotated[str, BeforeValidator(str)]


class BankAccountInformation(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    user_id: Optional[PyObjectId] = Field(alias="user_id", default=None)
    bank_id: Optional[PyObjectId] = Field(alias="bank_id", default=None)
    number_of_account: Optional[int] = Field(alias="number_of_account", default=None)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class AllBankAccount(BaseModel):
    list_of_bank_account: list[BankAccountInformation] = Field(
        alias="list_of_bank_account", default=[]
    )
