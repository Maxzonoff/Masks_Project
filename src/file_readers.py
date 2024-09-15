import pandas as pd


def read_csv_file(file_path: str) -> list[dict]:
    """Функция чтения CSV файла."""
    transactions = pd.read_csv(file_path, sep=";").to_dict("records")

    for transaction in transactions:
        transaction['description'] = str(transaction['description'])

    return transactions


def read_excel_file(file_path: str) -> list[dict]:
    """Функция чтения EXCEL файла."""
    transactions = pd.read_excel(file_path).to_dict("records")
    for transaction in transactions:
        transaction['description'] = str(transaction['description'])

    return transactions
