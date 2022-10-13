"""EX07 - Dictionary Utils - Tests."""
__author__: str = "730575822"


from dictionary import invert, favorite_color, count
import pytest


def test_invert_use_one() -> None:
    """Use case: given a dict of str : str, returns a dict with the keys as values and vice versa."""
    xs: dict[str, str] = {"A": "Z", "B": "Y", "C": "X"}
    assert invert(xs) == {"Z": "A", "Y": "B", "X": "C"}


def test_invert_use_two() -> None:
    """Use case: given a dict of str : str, returns a dict with the keys as values and vice versa."""
    xs: dict[str, str] = {"Hi!": "Hello", "Hello": "Hi!"}
    assert invert(xs) == {"Hello": "Hi!", "Hi!": "Hello"}


def test_invert_edge() -> None:
    """Edge case: given a dict with duplicate values, raises a KeyError."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def favorite_color_use_one() -> None:
    """Use case: given a dict of people and their favorite colors, returns the most popular favorite."""
    xs: dict[str, str] = {"Victoria": "blue", "Diane": "purple", "Serena": "yellow", "Tracy": "purple"}
    assert favorite_color(xs) == "purple"


def favorite_color_use_two() -> None:
    """Use case: given a dict with two most popular favorites, returns the one that appeared first."""
    xs: dict[str, str] = {"Evan": "pink", "Victoria": "blue", "Omar": "blue", "Serena": "pink"}
    assert favorite_color(xs) == "pink"


def favorite_color_edge() -> None:
    """Edge case: given an empty dictionary, returns an empty dictionary."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == {}


def count_use_one() -> None:
    """Use case: given a list of duplicate strings, returns a dict with the string and how often it appears."""
    xs: list[str] = ["Hello", "Hello", "blue skies", "green grass", "green grass"]
    assert count(xs) == {"Hello": 2, "blue skies": 1, "green grass": 2}


def count_use_two() -> None:
    """Use case: given a list of string with no duplicates, returns a dict with each string assigned to 1."""
    xs: list[str] = ["Hello", "blue skies", "green grass"]
    assert count(xs) == {"Hello": 1, "blue skies": 1, "green grass": 1}


def count_edge() -> None:
    """Edge case: given an empty list, returns an empty dictionary."""
    xs: list[str] = []
    assert count(xs) == {}