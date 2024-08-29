# Trading Bot
This is a simple trading bot that uses playwright to attempt to make trades on the stock market.

It exposes a rest API to allow for the bot to be controlled.

## Installation
Prerequisites:
Docker
or
Poetry

### Docker
```bash
docker build -t trading-bot .
docker run -p 8000:8000 trading-bot
```

### Poetry
```bash
poetry install
poetry run uvicorn main:app --reload
```

Your username and password for your broker should be set in the environment variables `BROKER_USERNAME` and `BROKER_PASSWORD`.
