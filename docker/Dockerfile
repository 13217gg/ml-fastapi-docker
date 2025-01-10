FROM python:3.12-slim

WORKDIR /app

# Install system dependencies required for psycopg2
# Always failed building postgress in docker, got following lines from AI
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY docker/requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

EXPOSE 12347

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "12347"]