from unittest.mock import patch

import pytest

from src.external_api import get_transaction_amount


def test_get_transaction_amount_bad_code(usd_transaction):
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 500
        with pytest.raises(Exception):
            get_transaction_amount(usd_transaction)


def test_get_transaction_amount_bad_json(usd_transaction):
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {}
        with pytest.raises(Exception):
            get_transaction_amount(usd_transaction)


def test_get_transaction_amount_with_request(usd_transaction):
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"result": 30.5}
        assert get_transaction_amount(usd_transaction) == 30.5


def test_get_transaction_amount_without_request(rub_transaction):
    assert get_transaction_amount(rub_transaction) == 8221.37


def test_get_transaction_without_amount(transaction_without_amount):
    with pytest.raises(ValueError):
        get_transaction_amount(transaction_without_amount)


def test_get_transaction_without_currency(transaction_without_currency):
    with pytest.raises(ValueError):
        get_transaction_amount(transaction_without_currency)


def test_get_transaction_unknown_currency(unknown_currency_transaction):
    with pytest.raises(ValueError):
        get_transaction_amount(unknown_currency_transaction)
