from fastapi import FastAPI

from config.db import SQL_Base, engine
from routes import user_route

SQL_Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(user_route.router, prefix="/api/v1/user")


@app.get("/")
async def main():
    return {"message": "Dozie Ecommerce API"}
