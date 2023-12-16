from __future__ import annotations

from pydantic import BaseModel, Field

class BaseAccount(BaseModel):
    account_name: str = Field(..., description="Account name of the bank account")
    user_id: str = Field(..., description="User id of the bank account")
    bank_id: str = Field(..., description="Bank id of the bank account")
    