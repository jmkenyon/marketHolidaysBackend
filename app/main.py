from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.holidays.router import router as holidays_router

app = FastAPI()

# Allow Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(holidays_router)


