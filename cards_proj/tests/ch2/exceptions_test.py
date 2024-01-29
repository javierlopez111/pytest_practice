import cards
import pytest


def test_no_path_raises_exception():
    # missing path within CardsDB() give the exception
    with pytest.raises(TypeError):
        cards.CardsDB()


def test_raises_exception_with_info():
    match_regex = "missing 1 .* positional argument"
    with pytest.raises(TypeError, match=match_regex):
        cards.CardsDB()


def test_raises_exception_with_info_alt():
    with pytest.raises(TypeError) as exc_info:
        cards.CardsDB()
    expected = "missing 1 required positional"

    assert expected in str(exc_info.value)