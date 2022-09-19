"""An exercise to practice list utility functions."""
__author__: str = "730575822"

def all(intlist: list[int], singleint: int) -> bool:
    """Evaluates whether all ints in the list are the given int."""
    i: int = 0
    while i < len(intlist):
        if intlist[i] == singleint:
            i += 1
        elif len(intlist) == 0:
            return False
        else:
            return False
    return True
# still returns true if the list is empty, w/o elif. ask in OH

def max(input: list[int]) -> int:
    """Returns largest value of a list of integers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    index: int = 0
    while i < len(input):
        if input[i] > index:
            index = input[i]
        i += 1 
    return index

def is_equal(firstlist: int, secondlist: int) -> bool:
    """Based on deep equality, checks to see if two lists are exactly equal."""
    if firstlist == secondlist:
        return True
    else:
        return False

