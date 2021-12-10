from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserIn(BaseModel):
    quater: int
    origin: str
    dest: str
    numOfTicket: int


class UserOut(BaseModel):
    airline: str
    price: float

@app.get

@app.post
