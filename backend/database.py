import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
import psycopg2

# Retrieve the database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Check if DATABASE_URL is set
if not DATABASE_URL:
    print("Error: DATABASE_URL environment variable is not set.")
    exit(1)

try:
    # Attempt to connect to the database
    connection = psycopg2.connect(DATABASE_URL)
    print("Database connection successful!")

except psycopg2.OperationalError as e:
    # Handle operational errors (e.g., connection issues)
    print("OperationalError: Unable to connect to the database.")
    print(f"Details: {e}")

except psycopg2.ProgrammingError as e:
    # Handle programming errors (e.g., wrong SQL syntax)
    print("ProgrammingError: There was an issue with the database operation.")
    print(f"Details: {e}")

except Exception as e:
    # Handle any other exceptions
    print(f"Database connection failed: {e}")

finally:
    # Close the connection if it was established
    if 'connection' in locals() and connection:
        connection.close()
        print("Database connection closed.")

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
