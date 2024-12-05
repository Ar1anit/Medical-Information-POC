# Frontend Dockerfile
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files from the frontend folder into the container
COPY . /app

# Expose the Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "frontend.py", "--server.port=8501", "--server.address=0.0.0.0"]
