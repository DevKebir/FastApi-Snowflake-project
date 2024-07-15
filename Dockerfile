# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.12.1
FROM python:${PYTHON_VERSION}-slim as base

ENV APP_HOME=/app
WORKDIR ${APP_HOME}
# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

COPY . /app