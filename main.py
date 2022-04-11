from fastapi import FastAPI
from db.base import database
from endpoints import users, auth, apples, buy_apples
from fastapi.testclient import TestClient
import uvicorn

app = FastAPI(
    title="Apple API", description="Apple API", version="0.1.0")
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(apples.router, prefix="/apples", tags=["Apples"])
app.include_router(
    buy_apples.router, prefix="/buy_apple", tags=["Buy apples"])


client = TestClient(app)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
