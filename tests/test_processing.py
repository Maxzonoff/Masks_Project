from src.processing import filter_by_state, sort_by_date
from .fixtures import list_dicts_date, list_dicts


def test_filter_by_state_default_state(list_dicts):
    assert filter_by_state(list_dicts) == [
        {"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"state": "EXECUTED"},
    ]


def test_filter_by_state_is_empty():
    assert filter_by_state([]) == []


def test_sort_by_date_is_empty():
    assert sort_by_date([]) == []


def test_sort_by_date_key_date(list_dicts_date, reverse=True):
    assert sort_by_date(list_dicts_date, ascending=True) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
