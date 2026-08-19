from fastapi import FastAPI
from backend.routes import cpu

app = FastAPI(
    title="KernelSense API",
    description="Linux system monitoring and diagnostics backend",
    version="1.0.0"
)
app.include_router(cpu.router, prefix="/api/v1")


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
