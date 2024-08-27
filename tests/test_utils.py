from src.utils import get_operations_info


def test_get_info_json_object():
    file_name = "oper.json"
    result = get_operations_info(file_name)
    assert result == []
