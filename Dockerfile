FROM python:3.11-slim

RUN apt-get update && apt-get install -y vim
RUN pip install --upgrade pip
RUN pip install poetry gunicorn

WORKDIR /app/

COPY pyproject.toml .
COPY poetry.lock .
COPY setup.cfg .

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY backend/ .

EXPOSE 8000/tcp

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000"]
