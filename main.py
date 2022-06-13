from fastapi import FastAPI

from config.db import SQL_Base, engine

SQL_Base.metadata.create_all(engine)

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Dozie Ecommerce API"}
