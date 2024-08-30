FROM python:3.12
WORKDIR /app
RUN apt-get update && apt-get install -y xvfb
ENV POETRY_VIRTUALENVS_CREATE=false

RUN python -m ensurepip --upgrade

RUN pip install --no-cache-dir  poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN poetry run playwright install
RUN poetry run playwright install-deps
RUN nohup Xvfb :40 -ac & export DISPLAY=:40

COPY . .

CMD ["/bin/bash", "./entrypoint.sh"]