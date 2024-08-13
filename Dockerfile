# Stage 1: Build stage
FROM python:3.12.5-bookworm AS builder

# Set work directory for the build stage
WORKDIR /showtime-plus

# Copy all files into the build stage
COPY . /showtime-plus

# Final stage
FROM python:3.12.5-bookworm

# Set work directory for the production stage
WORKDIR /showtime-plus

# Copy only the necessary files from the build stage
COPY --from=builder /showtime-plus /showtime-plus

# Install build dependencies
RUN pip install --no-cache-dir -r requirements/requirements.txt

# Compile assets or run any other build steps (e.g., CSS/JS minification)
RUN python manage.py collectstatic --noinput

# Expose networking ports
EXPOSE 80
EXPOSE 8000

# Run project
CMD gunicorn -b 0.0.0.0:80 -b 0.0.0.0:8000 core.wsgi