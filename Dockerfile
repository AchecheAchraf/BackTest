# Use Python as base image
FROM python:3.11.9-slim as build-stage

# Set working directory
WORKDIR /app

# Copy all files from current directory to work directory
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
