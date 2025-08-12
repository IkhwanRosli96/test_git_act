import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Hello from Docker CI sample! Please working!!!"}

@app.get("/health")
def health():
    return {"healthy": True}

# ⚠️ TEST ONLY
@app.get("/show-secret")
def show_secret():
    secret_value = os.getenv("MY_TEST_SECRET", "Secret not set")
    return {"MY_TEST_SECRET": secret_value}