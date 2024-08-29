FROM python:3.12

RUN python -m ensurepip --upgrade

RUN pip install --no-cache-dir  poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN poetry run playwright install
RUN poetry run playwright install-deps

COPY . .

CMD ["poetry", "run", "fastapi", "run", "app/main.py"]