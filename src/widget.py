from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_number_account_card: str) -> str:
    """Функция принимает тип и номер карты и счета и возвращает замаскированный номер"""

    str_alpha = ""
    str_number = ""
    for i in type_number_account_card:
        if i.isdigit():
            str_number += i
        else:
            str_alpha += i

    if len(str_number) == 16:

        return f"{str_alpha} {get_mask_card_number(str_number)}"
    else:
        return f"{str_alpha} {get_mask_account(str_number)}"


def get_date(date: str) -> str:
    return ".".join(reversed(date[0:10].split("-")))


print(get_date("2024-03-11T02:26:18.671407"))
