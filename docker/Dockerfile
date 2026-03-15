# docker/Dockerfile
# This Dockerfile sets up the environment for the Streamlit dashboard of the AI Business Intelligence Agent. 
# It uses the official Python 3.11 slim image, 
# installs the required dependencies, and runs the Streamlit application.

# Base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run the Streamlit application
CMD ["streamlit", "run", "src/dashboard/dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
