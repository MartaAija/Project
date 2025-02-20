# Use Python 3.12 as the base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt update && apt install -y libpq-dev gcc && apt clean

# Install pip and update it
RUN pip install --upgrade pip

# Copy the requirements file and install dependencies
COPY backend/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy the application code (including backend directory)
COPY . .

# Expose the port
EXPOSE 8080

# Use Gunicorn instead of Flask's development server
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "main:app"]
