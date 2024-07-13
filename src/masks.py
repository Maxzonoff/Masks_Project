def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты."""
    if len(card_number) < 16:
        raise ValueError("Неверная длина карты")

    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета."""

    if len(account_number) < 20:
        raise ValueError("Неверная длина счета")

    return f"**{account_number[-4:]}"
