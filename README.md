# Python FastAPI Service with Allure Reporting

## Service

A simple FastAPI service with two endpoints:

- `GET /` — Returns a hello world message.
- `POST /items/` — Accepts a JSON item (name, value) and returns it.

## Testing

Uses `pytest` and `allure-pytest` for reporting.

### Install dependencies

```bash
pip install fastapi uvicorn pytest allure-pytest
```

### Run the service

```bash
uvicorn service:app --reload
```

### Run the tests with Allure reporting

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

> Make sure you have [Allure commandline](https://docs.qameta.io/allure/#_installing_a_commandline) installed for `allure serve`.
````