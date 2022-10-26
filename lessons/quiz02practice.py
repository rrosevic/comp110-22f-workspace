"""Code-writing practice for quiz 02."""


def odd_and_even(xs: list[int]) -> list[int]:
    """Returns numbers that are odd with an even index."""
    result: list[int] = []
    i: int = 0
    while i < len(xs):
        for x in xs:
            if x % 2 != 0 and i % 2 == 0:
                result.append(xs[i])
        i += 1
    return result
print(odd_and_even([2, 9, 4, 17, 9, 10, 15, 13, 14, 21]))
print(odd_and_even([1, 1, 0, 1]))


def vowels_and_threes(string: str) -> str:
    """Returns vowels and chars at every third index."""
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    result: str = ""
    i: int = 0
    is_vowel: bool = False
    while i < len(string):
        for v in vowels:
            if v == string[i]:
                result += string[i]
            if v == string[i] and i % 3 == 0:
                result = ""
        if i % 3 == 0:
            result += string[i]
        i += 1
    return result
# print(vowels_and_threes("aeiou"))
# print(vowels_and_threes("hello world"))
def vowels_and_three(string: str) -> str:
    """Returns vowels or chars at every third index of a given string."""
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    result: str = ""
    if_vowel: bool = False
    i: int = 0
    while i < len(string):
        if_vowel = False
        for v in vowels:
            if v == string[i]:
                if_vowel = True
        if if_vowel and i % 3 == 0:
            result += ""
        elif i % 3 == 0:
            result += string[i]
        elif if_vowel:
            result += string[i]
        i += 1
    return result
# print(vowels_and_three("aeiou"))
# print(vowels_and_three("hello world"))
