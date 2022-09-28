"""EX05 - List Utility Functions."""
__author__: str = "730575822"


def only_evens(intlist: list[int]) -> list[int]:
    """Returns a list of the even numbers from a given list of integers."""
    i: int = 0
    newlist: list[int] = []
    while i < len(intlist):
        if intlist[i] % 2 == 0:
            x: int = intlist[i]
            newlist.append(x)
        i += 1
    return newlist


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Puts two lists together in a single lsit."""
    third_list: list[int] = first_list + second_list
    return third_list


def sub(intlist: list[int], start_ind: int, end_ind: int) -> list[int]:
    """Makes a list of integers from the given indicies of the first list."""
    list_returned: list[int] = []
    if len(intlist) == 0 or start_ind >= len(intlist) or end_ind <= 0:
        return list_returned
    if start_ind < 0:
        start_ind = 0
    if end_ind > len(intlist):
        end_ind = len(intlist)
    x: int = intlist[start_ind]
    y: int = intlist[end_ind - 1]

    list_returned.append(x)
    list_returned.append(y)

    return list_returned
