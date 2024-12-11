import os
from dotenv import load_dotenv
from pathlib import Path
import logging

# Load environment variables from a .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Setting up logging for better traceability
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Fetching environment variables with default values
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

# Ensuring that essential environment variables are loaded
if not DATABASE_URL:
    logger.warning("DATABASE_URL is not set in the .env file. Defaulting to sqlite:///./test.db.")
    DATABASE_URL = "sqlite:///./test.db"

if not SECRET_KEY:
    logger.error("SECRET_KEY is not set in the .env file! This is critical for app security.")
    raise ValueError("SECRET_KEY is required for the application to function properly.")

logger.info("Environment variables loaded successfully.")
