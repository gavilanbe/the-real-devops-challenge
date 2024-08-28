# Build stage
FROM python:3.9-alpine AS builder

WORKDIR /app
COPY webserver.py .

# Run stage
FROM python:3.9-alpine

WORKDIR /app

RUN apk add --no-cache curl && \
    adduser -D appuser && \
    chown -R appuser:appuser /app

COPY --from=builder /app/webserver.py .

USER appuser

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000 || exit 1

ENTRYPOINT ["python", "webserver.py"]
CMD ["--host", "0.0.0.0", "--port", "8000"]