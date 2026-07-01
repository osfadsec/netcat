# ---- Builder stage ----
FROM python:3.13-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

# ---- Runtime stage ----
FROM python:3.13-slim

WORKDIR /app

# Only the built virtualenv from the builder stage
COPY --from=builder /app/.venv /app/.venv

# Only the application files needed at runtime
COPY app.py netcat_core.py ./
COPY templates ./templates
COPY static ./static

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 5000

CMD ["python", "app.py"]
