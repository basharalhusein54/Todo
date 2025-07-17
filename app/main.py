from fastapi import FastAPI

from app.db.database import engine
from app.api.todo import router as todos_router
from app.models.todo import Base as TodosModel
from app.api.auth import router as auth_router
app = FastAPI()
TodosModel.metadata.create_all(engine)
app.include_router(todos_router)
app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "Home"}