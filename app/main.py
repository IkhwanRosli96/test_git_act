from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Hello from Docker CI sample!"}

@app.get("/health")
def health():
    return {"healthy": True}