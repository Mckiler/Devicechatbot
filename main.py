import requests
from fastapi import FastAPI

app = FastAPI()
 
@app.get("/")
async def root():
    # url = "https://openapi.botnoi.ai/botnoi/sentiment?keyword=undefined"
    # headers = {
    #     'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTE4Mzk3MTAsImlkIjoiODczYmMyNGItNGI3Zi00NjBjLWEyMTEtMDNjMTdkY2Y5Njk4IiwiaXNzIjoiU0pkOWRBdGJwUXA0YkcxYlFSb2dRek9SOTRlRE5kaHUiLCJuYW1lIjoiUGF0IiwicGljIjoiaHR0cHM6Ly9wcm9maWxlLmxpbmUtc2Nkbi5uZXQvMGh2SlBzQmJ1YktXVnRDajFUT0JoV01sRlBKd2dhSkM4dEZUZ3hBa0VDY0FkRVBXZ3lCR1V6QUV3SWNGUVZhR2htVW00MVZFcFpJd1ZKIn0.SK3xDx-Inq9NSPXeQNQItDmdV7WHurDg_1wYb4vaQMk'
    # }
    # url = "http://192.168.143.119/on" 
    url = "http://192.168.2.40/on" 
    
    response = requests.request("GET", url)
    
    # print(response.text)
    return {"Hello": "World"}

@app.get("/on")
async def root():
    # url = "https://openapi.botnoi.ai/botnoi/sentiment?keyword=undefined"
    # headers = {
    #     'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTE4Mzk3MTAsImlkIjoiODczYmMyNGItNGI3Zi00NjBjLWEyMTEtMDNjMTdkY2Y5Njk4IiwiaXNzIjoiU0pkOWRBdGJwUXA0YkcxYlFSb2dRek9SOTRlRE5kaHUiLCJuYW1lIjoiUGF0IiwicGljIjoiaHR0cHM6Ly9wcm9maWxlLmxpbmUtc2Nkbi5uZXQvMGh2SlBzQmJ1YktXVnRDajFUT0JoV01sRlBKd2dhSkM4dEZUZ3hBa0VDY0FkRVBXZ3lCR1V6QUV3SWNGUVZhR2htVW00MVZFcFpJd1ZKIn0.SK3xDx-Inq9NSPXeQNQItDmdV7WHurDg_1wYb4vaQMk'
    # }
    # url = "http://192.168.143.119/on" 
    url = "http://192.168.2.40/on" 
    
    response = requests.request("GET", url)
    
    # print(response.text)
    return {"Hello": "World"}

@app.get("/off")
async def root():
    # url = "https://openapi.botnoi.ai/botnoi/sentiment?keyword=undefined"
    # headers = {
    #     'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTE4Mzk3MTAsImlkIjoiODczYmMyNGItNGI3Zi00NjBjLWEyMTEtMDNjMTdkY2Y5Njk4IiwiaXNzIjoiU0pkOWRBdGJwUXA0YkcxYlFSb2dRek9SOTRlRE5kaHUiLCJuYW1lIjoiUGF0IiwicGljIjoiaHR0cHM6Ly9wcm9maWxlLmxpbmUtc2Nkbi5uZXQvMGh2SlBzQmJ1YktXVnRDajFUT0JoV01sRlBKd2dhSkM4dEZUZ3hBa0VDY0FkRVBXZ3lCR1V6QUV3SWNGUVZhR2htVW00MVZFcFpJd1ZKIn0.SK3xDx-Inq9NSPXeQNQItDmdV7WHurDg_1wYb4vaQMk'
    # }
    # url = "http://192.168.143.119/on" 
    url = "http://192.168.2.40/off" 
    
    response = requests.request("GET", url)
    
    # print(response.text)
    return {"Hello": "World"}