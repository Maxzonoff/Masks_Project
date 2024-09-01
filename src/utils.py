import json
import logging
import typing

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("logs/log_utils.log", mode="w+")
logger.addHandler(handler)
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
handler.setFormatter(formatter)


def get_operations_info(file_path: str) -> list[typing.Any]:
    """Функция принимающая путь до файла и возвращающая python объект. """
    try:
        with open(file_path) as f:
            data_info = json.load(f)
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден")
        return []
    except json.JSONDecodeError:
        logger.error(f"Не верный формат json {file_path}")
        return []

    if not isinstance(data_info, list):
        logger.warning(f"json должен содержать список, а содержит {type(data_info)}")
        return []
    logger.info("Файл загружен")
    return data_info
