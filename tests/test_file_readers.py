import pytest

from src.file_readers import read_csv_file, read_excel_file


@pytest.fixture()
def file_path_not_found():
    return 'data/fake'


@pytest.fixture()
def file_path_wrong_data():
    return 'tests/test_files/bad_data.json'


def test_read_csv_file_not_found(file_path_not_found):
    with pytest.raises(FileNotFoundError):
        read_csv_file(file_path_not_found)


def test_read_excel_file_not_found(file_path_not_found):
    with pytest.raises(FileNotFoundError):
        read_excel_file(file_path_not_found)


def test_read_excel_file_wrong_data(file_path_wrong_data):
    with pytest.raises(ValueError):
        read_excel_file(file_path_wrong_data)
