from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="AI Adaptive Diagnostic Engine",
    description="Adaptive testing system using Item Response Theory",
    version="1.0"
)
app.include_router(router)