import pytest
from src.generators import card_number_generator


@pytest.mark.parametrize('start', [-1, 10 ** 17])
def test_card_number_generator_invalid_start(start):
    with pytest.raises(ValueError):
        next(card_number_generator(start, 9999_9999_9999_9999))
# нужен тест на неправильны стоп и тест если старт больше чем стоп

def test_card_number_generator():
    c = card_number_generator(9998, 10003)
    assert next(c) == '0000 0000 0000 9998'
    assert next(c) == '0000 0000 0000 9999'
    assert next(c) == '0000 0000 0001 0000'
    assert next(c) == '0000 0000 0001 0001'
    assert next(c) == '0000 0000 0001 0002'
    assert next(c) == '0000 0000 0001 0003'
    with pytest.raises(StopIteration):
        next(c)
