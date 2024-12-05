# Backend Dockerfile
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    poppler-utils \
    build-essential \
    g++ \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY ../requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the backend code
COPY . /app

# Expose the Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
