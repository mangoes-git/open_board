from fastapi import FastAPI
from app.routes import users, messages

import app.models as models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(users.router)
app.include_router(messages.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
