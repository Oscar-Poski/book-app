FROM python:3.12-slim

# Evita bytecode y mantiene logs “unbuffered”
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencias del sistema para psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
  && rm -rf /var/lib/apt/lists/*

# Requisitos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código
COPY . /app
ENV PYTHONPATH=/app

# Uvicorn se define en docker-compose (command:)
