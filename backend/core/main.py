from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from .config import config
from .db.databases import get_session, engine
from .db.models import *
from .routes.user import user_route
from .routes.documents import documents_route

app = FastAPI()

app.mount("/documents", StaticFiles(directory="documents"), name="documents")

app.include_router(user_route, prefix="/api/user")
app.include_router(documents_route, prefix="/api/documents")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=[config.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create tables inside database
Base.metadata.create_all(engine)