import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

# Database URL (ensure the password is correct)
DATABASE_URL = os.getenv("DATABASE_URL")

# Create an engine with connection pooling
engine = create_engine(DATABASE_URL, poolclass=QueuePool, pool_size=5, max_overflow=10, pool_timeout=30)

# Base class for declarative models
Base = declarative_base()

# Session maker for database interaction
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to create the tables if not already created
def init_db():
    # Creates all the tables defined in the models
    Base.metadata.create_all(bind=engine)
