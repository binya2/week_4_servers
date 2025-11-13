import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

import utils

file_name = "names.txt"
app = FastAPI()
class CaesarBody(BaseModel):
    text: str = ""
    offset: int = 0
    mode:str =  "encrypt" or "decrypt"

class DecryptBody(BaseModel):
    text: str = ""



@app.get("/test")
def get_items():
    return {"msg": "hi from test"}


@app.get("/test/{usrename}")
def get_items(usrename: str):
    utils.append_to_file(file_name, usrename)
    return {"msg": "saved user"}


@app.post("/caesar")
def caesar(caesar: CaesarBody):
    pass

@app.get("/fence/encrypt?text=text_to_encrypt")
def encrypt_text(text: str):
    pass

@app.post("/fence/decrypt")
def decrypt_text(decrypt_body: DecryptBody):
    pass




if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
