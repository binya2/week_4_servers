import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def get_items():
    return { "msg": "hi from test"}



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
