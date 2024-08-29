_disclaimer:  This project is for resource purposes only and may violate local laws.  Ensure that you are aware of what you are doing, and use at your own risk_
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
