import time
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

import utils
from endpoints_data_manager import load_endpoint

file_name = "names.txt"
app = FastAPI()


class CaesarBody(BaseModel):
    text: str = ""
    offset: int = 0
    mode: str = "encrypt" or "decrypt"


class FenceBody(BaseModel):
    text: str = ""


@app.get("/test")
def get_msg_test():
    total_time = f"{(abs(time.perf_counter() - time.perf_counter())):.8f}"
    load_endpoint("/test","GET", total_time)
    print(total_time)
    return {"msg": "hi from test"}


@app.get("/test/{username}")
def get_msg_user(username: str):
    start_time = time.perf_counter()
    utils.append_to_file(file_name, username)
    total_time = f"{(start_time - time.perf_counter()):.8f}"
    load_endpoint("/test/{username}","GET", total_time)
    return {"msg": "saved user"}


@app.post("/caesar")
def caesar(caesar_body: CaesarBody):
    start_time = time.perf_counter()
    sign = 1 if caesar_body.mode == "encrypt" else -1
    key = caesar_body.offset * sign

    text_after_proses: str = utils.caesar_cipher(caesar_body.text, key)
    sign_mag: str = "encrypted_text" if sign == 1 else "decrypted_text"
    total_time = f"{(start_time - time.perf_counter()):.8f}"
    load_endpoint("/caesar", "POSP", total_time)
    return {sign_mag: text_after_proses}


@app.get("/fence/encrypt")
def fence_encrypt_text(text: str):
    start_time = time.perf_counter()
    encrypted_text = utils.fence_cipher_encrypt(text)
    total_time = f"{(start_time - time.perf_counter()):.8f}"
    load_endpoint("/fence/encrypt", "GET", total_time)
    return {"encrypted_text": encrypted_text}


@app.post("/fence/decrypt")
def fence_decrypt_text(fence_body: FenceBody):
    start_time = time.perf_counter()
    decrypted_text = utils.fence_cipher_decrypt(fence_body.text)
    total_time = f"{(start_time - time.perf_counter()):.8f}"
    load_endpoint("/fence/decrypt", "POSP", total_time)
    return {"decrypted": decrypted_text}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
