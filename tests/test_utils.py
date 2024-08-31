from src.utils import get_operations_info


def test_get_info_json_object():
    file_name = "tests/test_files/good.json"
    result = get_operations_info(file_name)
    assert result == [{}]


def test_get_json_empty():
    file_name = "operations.json"
    assert get_operations_info(file_name) == []


def test_get_operations_info_bad_file():
    assert get_operations_info('tests/test_files/bad.json') == []


def test_get_operations_info_not_list():
    assert get_operations_info('tests/test_files/not_list.json') == []
