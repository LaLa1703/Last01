from fastapi import FastAPI
from routes import auth, protected

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(protected.router, prefix="/content")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
