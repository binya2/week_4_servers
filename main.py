import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

import utils

file_name = "names.txt"
app = FastAPI()


class CaesarBody(BaseModel):
    text: str = ""
    offset: int = 0
    mode: str = "encrypt" or "decrypt"


class FenceBody(BaseModel):
    text: str = ""


@app.get("/test")
def get_items():
    return {"msg": "hi from test"}


@app.get("/test/{usrename}")
def get_items(usrename: str):
    utils.append_to_file(file_name, usrename)
    return {"msg": "saved user"}


@app.post("/caesar")
def caesar(caesar_body: CaesarBody):
    sign = 1 if caesar_body.mode == "encrypt" else -1
    key = caesar_body.offset * sign
    text_after_proses: str = utils.caesar_cipher(caesar_body.text, key)
    sign_mag: str = "encrypted_text" if caesar_body.mode == "encrypt" else "decrypted_text"
    return {sign_mag: text_after_proses}


@app.get("/fence/encrypt")
def fence_encrypt_text(text: str):
    encrypted_text = utils.fence_cipher_encrypt(text)
    return { "encrypted_text": encrypted_text }


@app.post("/fence/decrypt")
def fence_decrypt_text(fence_body: FenceBody):
    decrypted_text = utils.fence_cipher_decrypt(fence_body.text)
    return {"decrypted": decrypted_text}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
