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

# Accept build arguments
ARG SECRET_KEY
ARG DEBUG=false
ARG ALLOWED_HOSTS=*
ARG TMDB_API_KEY

# Set environment variables from build arguments
ENV SECRET_KEY=${SECRET_KEY}
ENV DEBUG=${DEBUG}
ENV ALLOWED_HOSTS=${ALLOWED_HOSTS}
ENV TMDB_API_KEY=${TMDB_API_KEY}

# Copy only the necessary files from the build stage
COPY --from=builder /showtime-plus /showtime-plus

# Install build dependencies
RUN pip install --no-cache-dir -r requirements/requirements.txt

# Expose networking ports
EXPOSE 80

# Run project
CMD python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn -b 0.0.0.0:80 core.wsgi