from src.filters import filter_by_description, count_by_category


def test_filter_by_description_empty():
    assert filter_by_description(transaction, 'карт')
    pass
