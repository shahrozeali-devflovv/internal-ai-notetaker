from fastapi import FastAPI

app = FastAPI(
    title="Internal AI NoteTaker API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Internal AI NoteTaker API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "backend",
    }