from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/api")
def read_root():
    return {
        "status": "online",
        "developer": "@lakshitpatidar",
        "timestamp": str(datetime.datetime.now()),
        "message": "System fully operational"
    }

@app.get("/api/hello")
def say_hello(name: str = "User"):
    return {"message": f"hn {name}, Api Is Active By @lakshitpatidar"}
  
