"""EX07 - Dictionary Utils - Dictionary."""
__author__: str = "730575822"


def invert(first_dict: dict[str, str]) -> dict[str, str]:
    """Turns the keys of a dictionary into values and vice versa."""
    result: dict[str, str] = {}
    for key in first_dict:
        if first_dict[key] in result:
            raise KeyError("cannot have duplicate strings")
        result[first_dict[key]] = key
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """From a list of people and their favorte colors, returns the more popular."""
    result: str = ""
    counter: dict[str, int] = {}
    for key in colors:
        if colors[key] in counter:
            counter[colors[key]] += 1
        else:
            counter[colors[key]] = 1
    most: int = 0
    for index in counter:
        if counter[index] > most:
            most = counter[index]
            result = index
    return result


def count(count_list: list[str]) -> dict[str, int]:
    """Given strings, returns a count of the number of times each str appeared."""
    result: dict[str, int] = {}
    for word in count_list:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

    