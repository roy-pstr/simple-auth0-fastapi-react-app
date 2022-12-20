FROM python:3.9-slim
LABEL maintainer="Roy Pasternak <roy@larium.ai>"

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

ENV POETRY_VERSION=1.2.0b3

RUN pip install -U pip \
    pip install poetry==$POETRY_VERSION
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /app/
WORKDIR /app

RUN poetry install --no-interaction --no-ansi --no-root

COPY . /app

EXPOSE 80

RUN chmod 777 scripts/run

CMD ["/bin/bash", "scripts/run"]