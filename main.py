from src.file_readers import read_csv_file, read_excel_file
from src.filters import filter_by_description
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_operations_info


def main():
    """Функция для использования приложения."""
    greeting = """Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    user_answer = input(f"{greeting} \n")

    while user_answer not in ["1", "2", "3"]:
        print("Не правильный ввод!\nПопробуйте еще раз:\n")
        user_answer = input()

    if user_answer == "1":
        print("Для обработки выбран JSON-файл:\n")
        res = get_operations_info("data/operations.json")
    elif user_answer == "2":
        print("Для обработки выбран CSV-файл:\n")
        res = read_csv_file("data/operations.csv")
    elif user_answer == "3":
        print("Для обработки выбран XLSX-файл:\n")
        res = read_excel_file("data/operations_excel.xlsx")

    filter_state = """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные статусы: 'EXECUTED', 'CANCELED', 'PENDING'."""
    user_answer_state = input(f"{filter_state}\n").upper()

    while user_answer_state not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f'Статус операции - "{user_answer_state}" не доступен! \nПопробуйте еще раз!\n')
        print("""Введите статус для фильтрации: \nEXECUTED, CANCELED, PENDING""")
        user_answer_state = input().upper()

    print(f"Операции отфильтрованы по статусу: {user_answer_state}")

    result = filter_by_state(res, user_answer_state)

    sort_data = "Отсортировать операции по дате? Да/Нет"
    print(sort_data)
    user_answer_date = input().lower()
    while user_answer_date not in ["да", "нет"]:
        print("Введите правильный ответ!")
        user_answer_date = input().lower()
    if user_answer_date == "да":
        print("Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию")
        user_answer_asc = input().lower()
        while user_answer_asc not in ["по возрастанию", "по убыванию"]:
            print("Введите правильный ответ! по возрастанию/по убыванию")
            user_answer_asc = input().lower()
        if user_answer_asc == "по возрастанию":
            result = sort_by_date(result, ascending=True)
        else:
            result = sort_by_date(result, ascending=False)

    print("Выводить только рублевые транзакции? Да / Нет")
    user_answer_curr = input().lower()
    while user_answer_curr not in ["да", "нет"]:
        print("Введите правильный ответ! Да/Нет")
        user_answer_curr = input().lower()
    if user_answer_curr == "да":
        result = filter_by_currency(result, "RUB")

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_answer_filter = input().lower()
    while user_answer_filter not in ["да", "нет"]:
        print("Введите правильный ответ! Да/Нет")
        user_answer_filter = input().lower()
    if user_answer_filter == "да":
        user_answer_word = input("Введите слово по которому фильтровать: ").lower()
        result = filter_by_description(result, user_answer_word)
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(result)}")
    print(result)


if __name__ == "__main__":
    main()
