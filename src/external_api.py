import os
import typing

import requests
from dotenv import load_dotenv


def get_transaction_amount(transaction: dict[str, typing.Any]) -> float:
    """Функция, обращается к API для получения курса."""
    load_dotenv()

    try:
        amount = float(transaction["operationAmount"]["amount"])
    except (KeyError, TypeError):
        raise ValueError("Не найден operationAmount.amount")

    try:
        currency = transaction["operationAmount"]["currency"]["code"]
    except KeyError:
        raise ValueError("Не найден operationAmount.currency.code")

    if currency == "RUB":
        return float(amount)
    if currency in ["USD", "EUR"]:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": os.getenv("API_KEY")}
        response = requests.get(url, headers=headers)
        status_code = response.status_code
        if status_code != 200:
            raise Exception(f"Ошибка сервера: {status_code}")

        try:
            return float(response.json()["result"])
        except KeyError:
            raise Exception("Отсутствует result")

    raise ValueError("Неизвестная валюта")
