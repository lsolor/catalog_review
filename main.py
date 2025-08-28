from fastapi import FastAPI
from api.routers import health

app = FastAPI(title="Catalog Review Service", version="1.0.0")

app.include_router(health.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
