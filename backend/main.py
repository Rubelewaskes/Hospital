import uvicorn
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from api.routers import all_routers
from auth.db import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(
    title="Стопапупа",
    lifespan=lifespan
)

for router in all_routers:
    app.include_router(router)


app.add_middleware(
        CORSMiddleware,["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
        allow_headers=[
            "Content-Type",
            "Set-Cookie",
            "Access-Control-Allow-Headers",
            "Access-Control-Allow-Origin",
            "Authorization",
            "Cookie",
        ],
        expose_headers=["Set-Cookie","X-Total-Count"],
    )


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)

#   raise HTTPException(
#     status_code=400,
#     detail="Didn't find doctor in database"
#   )