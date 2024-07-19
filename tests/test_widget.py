import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
        ("2018-09-12T21:27:25.241689", "12.09.2018"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
    ],
)
def test_get_date(date, expected):
    assert get_date(date) == expected
