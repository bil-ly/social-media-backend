from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
app = FastAPI()


class Post(BaseModel):
    title : str = "Welcome to my instagram buddy"
    content : str


@app.get("/")
async def root():
    return {"message": "HEllo Billy"}

@app.get("/name")
def getNames():
    return {"names": {"Abongile","Billy"}}

@app.post("/name")
async def addName(payload:Post):
    # Covert the model to dict
    post_dict = payload.dict()
    return {f"Post with title {post_dict['title']} successfully added"}


