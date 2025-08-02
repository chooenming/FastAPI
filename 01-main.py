from fastapi import FastAPI
from enum import Enum # use API to generate error for invalid input
import typing as t

# initializing FastAPI class
app = FastAPI()

"""
'/' called as Path
refers to the last part of the URL starting from the first '/'
https://example.com/items/foo
one '/' refers to https://example.com/
"""

@app.get("/")
def home_page():
    return {"message": "Hello World!"}

# define a path parameter
@app.get("/items/{item_id}")
# define function to be asynchronous
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "The current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

# # error because above mentioned must be integer
# # hence, have to put above
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "The current user"}

class ModelName(str, Enum):
    ALEXNET = "ALEXNET"
    RESNET = "RESNET"
    LENET = "LENET"

@app.get("/models/{model_name}")
# value of model_name can only be those defined in class ModelName
async def get_model(model_name: ModelName):
    if model_name == ModelName.ALEXNET:
        return {"model_name": model_name}
    elif model_name.value == "LENET":
        return {"model_name": model_name}
    else:
        return {"model_name": f"You have selected {model_name.value}"}

# makes file_path a file path (ends with '/')
# use path converter (:path)
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
"""
path example:
/home/chooenming/
"""

# Query Parameters
# Optional = optional parameters
dummy_db = [{"item_name": "t-shirt"},
            {"item_name": "shoe"},
            {"item_name": "watch"}]
@app.get("/items/")
async def read_items(skip: int=0, limit: int=10, optional_parameter: t.Optional[int]=None):
    """
    skip: number of items to skip
    limit: maximum number of items to return
    """
    return {"items": dummy_db[skip: skip+limit], "optional_parameter": optional_parameter}
# can use in browser: http://127.0.0.1:8000/items/?skip=0&limit=1
# for optional parameter: http://127.0.0.1:8000/items/?skip=1&limit=2&optional_parameter=55355

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: int, q: t.Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "user_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is a long description of the item."})
    return item
# example1: http://127.0.0.1:8000/users/1/items/13
# example2: http://127.0.0.1:8000/users/1/items/13?q=Choo%20En%20Ming&short=True

from pydantic import BaseModel

class Book(BaseModel):
    name: str
    author: str
    description: t.Optional[str] = None
    price: float

@app.post("/books/")
async def create_item(book: Book):
    return {"book": book}
# http://127.0.0.1:8000/books/ -> get error ("method not allowed") because it is app.post not app.get
# go to docs to try it