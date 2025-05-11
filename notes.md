# API_ DEVELOPMENT PYTHON       

## Basic API intro FASTAPI     
~~~
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "HEllo Billy"}

~~~     
### Suppose you want to retrive the body data     
~~~
From fastapi.params import Body
@app.post(payload: dict=(Body(...)))
~~~     

### Defining a schema    
~~~python
from pydantic import BaseModel
~~~