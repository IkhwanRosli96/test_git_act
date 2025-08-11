from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "This is automatically updated by the github actions again and again"}

@app.get("/health")
def health():
    return {"healthy": True}