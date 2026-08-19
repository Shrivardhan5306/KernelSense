from fastapi import FastAPI

from backend.routes import cpu
from backend.routes import memory
from backend.routes import storage
from backend.routes import process
from backend.routes import network
from backend.routes import files
from backend.routes import logs


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

app.include_router(
    process.router,
    prefix="/api/v1"
)

app.include_router(
    network.router,
    prefix="/api/v1"
)

app.include_router(
    files.router,
    prefix="/api/v1"
)

app.include_router(
    logs.router,
    prefix="/api/v1"
)
