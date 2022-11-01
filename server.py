from email import message
from enum import Enum
from fastapi import FastAPI, Path
app = FastAPI()

class AccountType(str, Enum):
    FREE = 'free'
    PRO = 'pro'

@app.get("/")
async def root():
    return {'message': 'testing use cars api'}

@app.get("/car/{id}")
async def root(id:int):
    return {"car_id":id}

@app.get("/account/{acc_type}/{months}")
async def account(acc_type:AccountType, months:int = Path(..., ge=3, le=12)):
    return {
        "message":"Account created",
        "account _type": acc_type,
        "months":months
    }


@app.get("/cars/price")
async def cars_by_price(min_price: int=0, max_price: int=100000):
    return {"message": f"Listing cars with prices between {min_price} and {max_price}"}

