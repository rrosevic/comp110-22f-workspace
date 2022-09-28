"""EX05 - Skeleton Code and Testing Setup // Unit Tests."""
__author__: str = "730575822"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_use() -> None:
    """Use case: given a list of integers in numerical order, returns even numbers."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_only_evens_edge_one() -> None:
    """Edge case: given an empty list, returns an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_edge_two() -> None:
    """Edge case: given a list with one odd integer, returns an empty list."""
    xs: list[int] = [1]
    assert only_evens(xs) == []


def test_concat_use() -> None:
    """Use case: given two lists in numerical order, returns a list of both."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [4, 5, 6]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6]


def test_concat_edge_one() -> None:
    """Edge case: Given an empty list and a list in numerical order, returns the second list."""
    xs: list[int] = []
    ys: list[int] = [1, 2, 3]
    assert concat(xs, ys) == [1, 2, 3]


def test_concat_edge_two() -> None:
    """Edge case: given two empty lists, returns an empty list."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_sub_use() -> None:
    """Use case: given a list of values, returns a list of numbers at given indicies (end: index -1)."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]


def test_sub_edge_one() -> None:
    """Edge case: given ints less/greater than given list, returns first and last indicies, respectively."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, -1, 5) == [10, 40]


def test_sub_edge_two() -> None:
    """Edge case: given two ints larger than list length, an empty list is returned."""
    xs: list[int] = [1, 2, 3, 4]
    assert sub(xs, 5, 5) == []