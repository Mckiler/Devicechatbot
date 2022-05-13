import requests
from fastapi import FastAPI

app = FastAPI()
 
@app.get("/")
async def root():
    url = "http://192.168.2.40/on" 
    response = requests.request("GET", url)
    return {"Hello": "World"}

@app.get("/on")
async def root():
    url = "http://192.168.2.40/on" 
    response = requests.request("GET", url)
    return {"Hello": "World"}

@app.get("/off")
async def root():
    url = "http://192.168.2.40/off" 
    response = requests.request("GET", url)
    return {"Hello": "World"}
