# Stage 1: Build
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
# Adding --no-cache-dir and upgrading pip for security
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim
WORKDIR /app

# NEW: Security Patching Step
# We update the OS packages to pull in the latest security fixes
USER root
RUN apt-get update && apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /root/.local /root/.local
COPY app.py .

ENV PATH=/root/.local/bin:$PATH
ENV APP_HOST=0.0.0.0

EXPOSE 5000
CMD ["python", "app.py"]