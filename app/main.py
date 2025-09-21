from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import SQLAlchemyError
from app.database.connection import engine

app = FastAPI(
    title="Orbit API",
    description="Personal calendar management system",
    version="0.1.0",
)

# Configure CORS for Flutter frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:8080",
    ],  # Flutter web ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Orbit API is running", "version": "0.1.0"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/db-check")
async def db_check():
    try:
        # Test the connection by connecting to the database
        async with engine.connect() as connection:
            await connection.close()
        return {"status": "Database connection successful"}
    except SQLAlchemyError as e:
        return {
            "status": "Database connection failed",
            "error": str(e),
            "error_type": type(e).__name__,
            "details": repr(e),
        }
    except Exception as e:
        return {
            "status": "Database connection failed",
            "error": str(e),
            "error_type": type(e).__name__,
            "details": repr(e),
        }
