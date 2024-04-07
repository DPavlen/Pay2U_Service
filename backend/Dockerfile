FROM python:3.11-slim as main

RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR /app

COPY ../pyproject.toml ../poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

RUN poetry install --no-root --only main


COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8100", "backend.wsgi"]