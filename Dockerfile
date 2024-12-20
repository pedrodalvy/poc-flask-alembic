# syntax=docker/dockerfile:1.4
FROM python:3.13-slim AS base

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

FROM base AS production

COPY pyproject.toml poetry.lock /app/

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=cache,target=/root/.cache/pypoetry \
    pip install --no-cache poetry && \
    poetry config virtualenvs.create false && \
    poetry install --only main

COPY src /app/src

CMD ["poetry", "run", "python", "src/app/app.py"]

FROM base AS development

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 POETRY_VIRTUALENVS_CREATE=false

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=cache,target=/root/.cache/pypoetry \
    pip install --no-cache poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /app/

RUN --mount=type=cache,target=/root/.cache/pypoetry poetry install

COPY src /app/src

RUN groupadd -r devgroup && useradd -r -g devgroup devuser && \
    chown -R devuser:devgroup /app

USER devuser

ENV PYTHONPATH=/app/src

CMD ["poetry", "run", "start"]
