from __future__ import annotations
from typing import Optional

from pydantic import BaseModel, Field

class StockData(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    symbol_name: str = Field(..., description="The name of the stock")
    current_price: float = Field(..., description="The open price of the stock")
    yesterday_price: float = Field(..., description="The close price of the stock")
    price_difference: float = Field(..., description="The price difference between yesterday and today")


class StockList(BaseModel):
    list_of_stocks: list[StockData] = []