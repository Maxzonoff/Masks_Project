from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_number_account_card: str) -> str:
    """Функция принимает тип и номер карты и счета и возвращает замаскированный номер"""

    str_alpha, str_number = type_number_account_card.rsplit(" ", 1)

    if len(str_number) == 16:
        return f"{str_alpha} {get_mask_card_number(str_number)}"

    return f"{str_alpha} {get_mask_account(str_number)}"


def get_date(date: str) -> str:
    return ".".join(reversed(date[0:10].split("-")))
