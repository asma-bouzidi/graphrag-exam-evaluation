# Use stable Debian bookworm to avoid mirror sync issues
FROM python:3.11-slim-bookworm

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install system dependencies with robust apt configuration
RUN echo 'Acquire::Retries "5";' > /etc/apt/apt.conf.d/80-retries \
    && echo 'APT::Get::Assume-Yes "true";' >> /etc/apt/apt.conf.d/80-retries \
    && echo "Acquire::http::Pipeline-Depth 0;" > /etc/apt/apt.conf.d/99custom \
    && echo "Acquire::http::No-Cache true;" >> /etc/apt/apt.conf.d/99custom \
    && echo "Acquire::BrokenProxy true;" >> /etc/apt/apt.conf.d/99custom \
    && apt-get update \
    && apt-get install -y --no-install-recommends --fix-missing \
       curl \
       poppler-utils \
       tesseract-ocr \
       tesseract-ocr-eng \
       tesseract-ocr-fra \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Create upload directory
RUN mkdir -p /app/uploads

# Expose port
EXPOSE 8083

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8083/health || exit 1

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8083", "--workers", "1"]
