from __future__ import annotations
import asyncio
from functools import lru_cache

from fastapi import APIRouter
import asyncio
from concurrent.futures import ThreadPoolExecutor
import yfinance as yf

from constant import Message
from models.stock import StockData, StockList

router = APIRouter(prefix="/api/v1", tags=["Stock API"])
STOCK_LIST = ["aapl", "msft", "tsla", "metv", "goog", "amzn", "fb", "nflx"]

# Use ThreadPoolExecutor to run synchronous code asynchronously
async def get_stock_data(name):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        stock = await loop.run_in_executor(pool, yf.Ticker, name)
        previous_price = await loop.run_in_executor(pool, lambda: stock.info['previousClose'])
        current_price = await loop.run_in_executor(pool, lambda: stock.info['open'])
        price_difference = current_price - previous_price
        return StockData(symbol=name, 
                         symbol_name=stock.info['shortName'], 
                         current_price=current_price, 
                         yesterday_price=previous_price, 
                         price_difference=price_difference)

async def get_stock_yahoo():
    tasks = [get_stock_data(name) for name in STOCK_LIST]
    stock_data = await asyncio.gather(*tasks)
    return StockList(list_of_stocks=stock_data)

# Convert get_news to async
@router.get("/get_stocks", responses = {404: {"model": Message}})
@lru_cache()
async def get_news():
    await get_stock_yahoo()


