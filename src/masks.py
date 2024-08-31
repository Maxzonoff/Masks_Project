import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("logs/log_masks.log", mode="w+")
logger.addHandler(handler)
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
handler.setFormatter(formatter)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты."""
    if len(card_number) < 16:
        logger.error("Неверная длина карты")
        raise ValueError("Неверная длина карты")

    card_number_mask = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info("Успешно замаскировали карту")
    return card_number_mask


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета."""

    if len(account_number) < 20:
        logger.error("Неверная длина счета")
        raise ValueError("Неверная длина счета")

    account_number_mask = f"**{account_number[-4:]}"
    logger.info("Успешно замаскировали счет")
    return account_number_mask
