import time

from fastapi import FastAPI
import pyotp
import os

from app.wealthsimple.wealthsimple import WealthSimple


app = FastAPI()
username = os.environ.get("BROKER_USERNAME")
password = os.environ.get("BROKER_PASSWORD")
secret = os.environ.get("BROKER_OTP_SECRET")
platform = WealthSimple(username, password, secret)
@app.get("/")
async def root():
    await platform.login()
    time.sleep(5)
    return {"message": "Hello World"}
