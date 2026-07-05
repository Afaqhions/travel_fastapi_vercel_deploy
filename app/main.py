from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from app.database import engine, Base
from app.routers import destinations

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Travel Destinations API")

@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")

app.mount("/static", StaticFiles(directory="static", html=True), name="static")
app.include_router(destinations.router)
