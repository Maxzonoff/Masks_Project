import pytest

from src.file_readers import read_csv_file, read_excel_file


@pytest.fixture()
def file_path_not_found():
    return "data/fake"


@pytest.fixture()
def file_path_wrong_data():
    return "tests/test_files/bad_data.json"


@pytest.fixture()
def file_path_csv():
    return "tests/test_files/test_good_data.csv"


@pytest.fixture()
def file_path_excel():
    return "tests/test_files/test_good_data.xlsx"


def test_read_csv_file_not_found(file_path_not_found):
    with pytest.raises(FileNotFoundError):
        read_csv_file(file_path_not_found)


def test_read_excel_file_not_found(file_path_not_found):
    with pytest.raises(FileNotFoundError):
        read_excel_file(file_path_not_found)


def test_read_excel_file_wrong_data(file_path_wrong_data):
    with pytest.raises(ValueError):
        read_excel_file(file_path_wrong_data)


def test_read_csv(file_path_csv):
    assert read_csv_file(file_path_csv) == [
        {
            "amount": 16210,
            "currency_code": "PEN",
            "currency_name": "Sol",
            "date": "2023-09-05T11:30:32Z",
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "id": 650703,
            "state": "EXECUTED",
            "to": "Счет 39745660563456619397",
        },
        {
            "amount": 29740,
            "currency_code": "COP",
            "currency_name": "Peso",
            "date": "2020-12-06T23:00:58Z",
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "id": 3598919,
            "state": "EXECUTED",
            "to": "Discover 0720428384694643",
        },
        {
            "amount": 30368,
            "currency_code": "TZS",
            "currency_name": "Shilling",
            "date": "2023-07-22T05:02:01Z",
            "description": "Перевод с карты на карту",
            "from": "Visa 1959232722494097",
            "id": 593027,
            "state": "CANCELED",
            "to": "Visa 6804119550473710",
        },
    ]
