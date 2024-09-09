import pandas as pd


def read_csv_file(file_path: str) -> list[dict]:
    """Функция чтения CSV файла."""
    transactions = pd.read_csv(file_path, sep=";")

    return transactions.to_dict("records")


def read_excel_file(file_path: str) -> list[dict]:
    """Функция чтения EXCEL файла."""
    transactions = pd.read_excel(file_path)

    return transactions.to_dict("records")
