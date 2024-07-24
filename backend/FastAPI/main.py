from typing import Union

from fastapi import FastAPI
import pymongo

import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# loading variables from .env file
load_dotenv()

# accessing and printing value
print(os.getenv("TEST_KEY"))

client = MongoClient(os.getenv("MONGO_CONNECTION"), server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
