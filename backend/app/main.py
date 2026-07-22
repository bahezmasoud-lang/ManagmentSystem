from fastapi import FastAPI

app = FastAPI(
    title="Employee Management System API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Employee Management System API is running!"
    }