from fastapi import FastAPI
from app.api.chat import router 
from app.api.extract import router as extract_router

app = FastAPI(title="AI Assistant Agent", version="1.0.0")

app.include_router(router, prefix="/chat")
app.include_router(extract_router, prefix="")

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Assistant Agent API!"}