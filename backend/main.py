import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi import HTTPException
from api.routers import all_routers
from starlette.middleware.cors import CORSMiddleware



app = FastAPI(
    title="Стопапупа"
)


for router in all_routers:
    app.include_router(router)

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
        allow_headers=[
            "Content-Type",
            "Set-Cookie",
            "Access-Control-Allow-Headers",
            "Access-Control-Allow-Origin",
            "Authorization",
        ],
    )


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)

#   raise HTTPException(
#     status_code=400,
#     detail="Didn't find doctor in database"
#   )