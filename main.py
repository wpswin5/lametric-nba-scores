from typing import Optional

from fastapi import FastAPI
from routers import teams, scores

app = FastAPI(
    title="NBA Scores API",
    description="API for retrieving NBA scores and game information",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Include routers
app.include_router(teams.router)
app.include_router(scores.router)


@app.get("/")
async def root():
    return {"message": "NBA Scores API - Visit /docs for documentation"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}