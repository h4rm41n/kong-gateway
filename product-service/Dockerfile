# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expose the API's port to the host machine
EXPOSE 8080

# Define the command to run the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
