from fastapi import FastAPI

app = FastAPI()


@app.get("/status", tags=["Status"])
async def status():
    return {"status": "up"}
