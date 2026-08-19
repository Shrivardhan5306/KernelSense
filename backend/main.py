from fastapi import FastAPI

from backend.routes import cpu
from backend.routes import memory
from backend.routes import storage


app = FastAPI(
    title="KernelSense API",
    description="Linux system monitoring and diagnostics backend",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "name": "KernelSense",
        "status": "running",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(
    cpu.router,
    prefix="/api/v1"
)

app.include_router(
    memory.router,
    prefix="/api/v1"
)

app.include_router(
    storage.router,
    prefix="/api/v1"
)
