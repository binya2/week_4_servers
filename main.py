import uvicorn
from fastapi import FastAPI

import utils

file_name = "names.txt"
app = FastAPI()

@app.get("/test")
def get_items():
    return { "msg": "hi from test"}

@app.get("/test/{usrename}")
def get_items(usrename: str):
    utils.append_to_file(file_name, usrename)
    return  { "msg": "saved user"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
