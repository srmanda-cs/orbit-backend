from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os
from dotenv import load_dotenv

# Determine the environment (default to development)
ENV = os.getenv("ENVIRONMENT", "development")

# Load the appropriate .env file
env_file = f".env.{ENV}"
load_dotenv(dotenv_path=env_file)

# Load database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Add debugging to see what we're loading
print(f"Environment: {ENV}")
print(f"Loading env file: {env_file}")
print(f"DATABASE_URL: {DATABASE_URL}")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Create the async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a session factory using async_sessionmaker
async_session = async_sessionmaker(engine, expire_on_commit=False)


# Dependency to get the database session
async def get_db():
    async with async_session() as session:
        yield session
