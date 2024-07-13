import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_invalid_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number('1234')


@pytest.mark.parametrize(
    'card_number, expected',
    [
        ('7000792289606361', '7000 79** **** 6361'),
        ('7000792289600000', '7000 79** **** 0000'),
        ('700079228960636100', '7000 79** **** 6100'),
        ('700079228960qwer', '7000 79** **** qwer')]
)
def test_get_mask_card_number_correct_masc(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_account_invalid_account_number():
    with pytest.raises(ValueError):
        get_mask_account('1234')


@pytest.mark.parametrize(
    'account_number, expected',
    [
        ('73654108430135874305', '**4305'),
        ('73654108430135873105', '**3105'),
        ('7365410843013587430510', '**0510'),
        ('736541084301358743qwer', '**qwer')]
)
def test_get_mask_account_correct_masc(account_number, expected):
    assert get_mask_account(account_number) == expected
