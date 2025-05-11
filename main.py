from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "HEllo Billy"}

@app.get("/name")
def getNames():
    return {"names": {"Abongile","Billy"}}

@app.post("/name")
async def addName(payload: dict=Body(...)):
    print(payload)
    return {"Name successfully added"}
