from fastapi import FastAPI, APIRouter
from auth.demo_auth import router

app = FastAPI()

api_router = APIRouter()

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
