import json


def get_operations_info(file_path: str) -> list:
    """Функция принимающая путь до файла и возвращающая python объект"""
    try:
        with open(file_path) as f:
            data_info = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    if not isinstance(data_info, list):
        return []
    return data_info
