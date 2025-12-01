from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.holidays.router import router as holidays_router
from app.xapi.router import router as xapi_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(holidays_router)
app.include_router(xapi_router)


