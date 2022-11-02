from enum import Enum
import shutil
from fastapi import FastAPI, File, Form, HTTPException, Path, Query, Body, UploadFile, status
from typing import Dict
from pydantic import BaseModel

app = FastAPI()

class InsertCar(BaseModel):
    brand: str
    model: str
    year: int

class InsertUser(BaseModel):
    username: str
    name: str


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
async def cars_by_price(min_price : int=Query(default=0, ge=0), max_price: int=Query(default=100000, le=100000)):
    return {"message": f"Listing cars with prices between {min_price} and {max_price}"}


@app.post("/cars", status_code=status.HTTP_201_CREATED)
async def new_car(car:InsertCar, user:InsertUser, code: int=Body(None)):

    if car.year >= 2024:
        raise HTTPException(
            status.HTTP_406_NOT_ACCEPTABLE,
            detail="The car does not exist yet yo...."
        )

    return {
        "car": car,
        "user": user,
        "code": code
    }

@app.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload(picture:UploadFile=File(...), brand:str=Form(...), model:str=Form(...)):
    with open("saved_file.png", "wb") as buffer:
        shutil.copyfileobj(picture.file, buffer)
    return {
        "brand": brand,
        "model": model,
        "file_name": picture.filename
    }