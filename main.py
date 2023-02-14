from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.item import item_router
from domain.test import test_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/hello")
# def hello():
#     return {"message": "Hello, Perigee!"}

app.include_router(item_router.router)
app.include_router(test_router.router)