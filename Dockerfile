# Base image with Python and Google Chrome
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    chromium-driver \
    chromium \
    && pip install --no-cache-dir -r requirements.txt

# Copy framework code
COPY . .

# Set default environment variables (can be overridden at runtime using -e)
ENV BASE_URL="https://www.saucedemo.com/"
ENV BROWSER_NAME="chrome"
ENV HEADLESS="true"

# Run pytest automatically when the container starts
ENTRYPOINT ["pytest", "-v", "--headless=true"]