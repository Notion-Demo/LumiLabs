from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database URL
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/task_management"

# Create engine with appropriate configurations
try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, pool_size=10, max_overflow=20)
    logger.info("Database engine created successfully.")
except SQLAlchemyError as e:
    logger.error(f"Error creating database engine: {e}")
    raise

# Create sessionmaker instance
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base for models
Base = declarative_base()

def get_db():
    """
    Dependency to get the database session.
    Use with dependency injection to handle session lifecycle.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def initialize_database():
    """
    Initialize the database by creating tables from all registered models.
    """
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully.")
    except SQLAlchemyError as e:
        logger.error(f"Error initializing database: {e}")
        raise
