import re
from collections import Counter


def filter_by_description(transactions: list[dict], search: str) -> list[dict]:
    """Функция поиска в описании."""
    filtered = []

    for transaction in transactions:
        if re.match(f".*{search}", transaction["description"], flags=re.IGNORECASE):
            filtered.append(transaction)

    return filtered


def count_by_category(transactions: list[dict], categories: list[str]) -> dict[str, int]:
    """Функция для подсчета описаний."""
    list_categories = []

    for transaction in transactions:
        if transaction["description"] in categories:
            list_categories.append(transaction["description"])

    return dict(Counter(list_categories))
