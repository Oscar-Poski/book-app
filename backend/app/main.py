from fastapi import FastAPI

app = FastAPI(
    title="My WebApp API",
    description="Backend REST API with FastAPI",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to My WebApp API 🚀"}
