# Use Python 3.12 as the base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install system dependencies (libpq-dev for psycopg2)
RUN apt update && \
    apt install -y libpq-dev gcc && \
    apt clean

# Install pip and update it
RUN pip install --upgrade pip

# Copy the requirements file and install Python dependencies
COPY backend/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy the application code to the container
COPY backend/. .

# Expose the port Flask or FastAPI will run on
EXPOSE 5000

# Set the default command to run the app
CMD ["python", "main.py"]
