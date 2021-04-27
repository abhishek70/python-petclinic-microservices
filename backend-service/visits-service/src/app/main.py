from fastapi import FastAPI

app = FastAPI(
    title="Visits Service",
    description="Visits service API documentation",
    version="1.0.0",
    docs_url="/api/v1/docs",
    openapi_url="/api/v1/openapi.json"
)


@app.get('/api/v1/status', tags=["health"])
def status():
    return {"status": "up"}
