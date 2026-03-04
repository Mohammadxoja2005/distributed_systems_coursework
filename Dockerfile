# 1. Use a modern Python version (3.12 is stable for 2026)
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Prevent Python from writing .pyc files and buffering output (Good for Docker logs)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 4. Install system dependencies for PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# 5. Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of your project code
COPY . /app/

# 7. Start the server (this matches your docker-compose command)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]