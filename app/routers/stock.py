from __future__ import annotations
import asyncio
from functools import lru_cache

from fastapi import APIRouter
import yfinance as yf

from constant import Message
from models.stock import StockData, StockList

router = APIRouter(prefix="/api/v1", tags=["Stock API"])
STOCK_LIST = ["aapl", "msft", "tsla", "metv", "goog", "amzn", "fb", "nflx"]

def get_stock_yahoo():
    for name in STOCK_LIST:
        stock = yf.Ticker(name)
        print(stock.info)
        previous_price = stock.info['previousClose']
        current_price = stock.info['open']
        price_difference = current_price - previous_price
        

@router.get("/get_stocks")
@lru_cache()
def get_news():
    get_stock_yahoo()


