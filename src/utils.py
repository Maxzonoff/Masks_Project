import json


def get_operations_info(file_path: str) -> list[dict]:
    '''Функция принимающая путь до файла и возвращающая python объект '''
    try:
        with open(file_path, 'r', encoding='utf8') as f:
            data_info = json.load(f)
            if type(data_info) is not list:
                return []
    except FileNotFoundError:
        return []
    else:
        return data_info


if __name__ == '__main__':
    print(get_operations_info(file_path='../data/operations.json'))
