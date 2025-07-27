from fastapi import FastAPI

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