# from src import masks, utils
#
# path_fake = "data/qwerty"
# print(utils.get_operations_info(path_fake))
#
# path_fake = "data/fake.json"
# print(utils.get_operations_info(path_fake))
#
# try:
#     print(masks.get_mask_card_number("12345"))
# except ValueError:
#     pass
# try:
#     print(masks.get_mask_account("1234"))
# except ValueError:
#     pass
import re

from src.file_readers import read_csv_file, read_excel_file
from src.processing import filter_by_state, sort_by_date
from src.utils import get_operations_info


def main():
    """ Функция для использования приложения. """
    greeting = '''Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла'''
    user_answer = input(f'{greeting} \n')

    while user_answer not in ['1', '2', '3']:
        print(f'Не правильный ввод! \nПопробуйте еще раз:\n')
        user_answer = input()
    else:
        if user_answer == '1':
            print('Для обработки выбран JSON-файл:\n')
            res = get_operations_info('data/operations.json')
        elif user_answer == '2':
            print('Для обработки выбран CSV-файл:\n')
            res = read_csv_file('data/operations.csv')
        elif user_answer == '3':
            print('Для обработки выбран XLSX-файл:\n')
            res = read_excel_file('data/operations_excel.xlsx')

    filter_state = '''Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные статусы: 'EXECUTED', 'CANCELED', 'PENDING'.\n'''
    user_answer_state = input(f'{filter_state}\n').upper()

    while user_answer_state not in ['EXECUTED', 'CANCELED', 'PENDING']:
        print(f'Статус операции - "{user_answer_state}" не доступен! \nПопробуйте еще раз!\n')
        print('''Введите статус для фильтрации: \nEXECUTED, CANCELED, PENDING\n''')
        user_answer_state = input().upper()
    else:
        if user_answer_state == 'EXECUTED':
            print(f'Операции отфильтрованы по статусу: "EXECUTED"\n')
        elif user_answer_state == 'CANCELED':
            print(f'Операции отфильтрованы по статусу: "CANCELED"\n')
        elif user_answer_state == 'PENDING':
            print(f'Операции отфильтрованы по статусу: "PENDING"\n')

    result = filter_by_state(res, user_answer_state)

    sort_data = '''Отсортировать операции по дате? Да/Нет'''
    user_answer_date = input().lower()
    while user_answer_date not in ['Да', 'Нет']:
        print('Введите правильный ответ!')
        print(sort_data)
    else:
        if user_answer_date == 'Да':
            print(sort_by_date(result, reverse=True))


if __name__ == '__main__':
    main()
