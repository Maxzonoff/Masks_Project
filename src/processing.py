def filter_by_state(list_dict: list, state="EXECUTED") -> list:
    """Функция сортрует словари в списках по значению ключа state."""
    set_value = []
    for val in list_dict:
        if val["state"] == state:
            set_value.append(val)

    return set_value


def sort_by_date(list_dict: list, date: str) -> list:
    """Функция сортировки дат по убыванию."""
    list_dict.sort(key=lambda x: x[date], reverse=True)

    return list_dict
