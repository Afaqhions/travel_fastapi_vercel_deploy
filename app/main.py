from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import engine, Base
from app.routers import destinations

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Travel Destinations API")

app.mount("/static", StaticFiles(directory="static", html=True), name="static")
app.include_router(destinations.router)
