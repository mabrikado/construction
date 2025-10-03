# Use official Python image
FROM python:3.11-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Copy and install dependencies
COPY construction/requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the entire Django project into the container
COPY construction/ /app/

# Expose port 8000
EXPOSE 8000

# Run migrations automatically before starting server
CMD ["sh", "-c", "python manage.py collectstatic --noinput && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]


