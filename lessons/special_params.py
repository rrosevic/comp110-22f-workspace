"""Examples of optional parameters and Union types."""

from typing import Union

def hello(name: Union[str, int, float] = "World") -> str:
    """A delightful greeting."""
    if isinstance(name, str):
        greeting += name
    elif isinstance(name, int):
        greeting: str = "Hello, " + str(name)
    else:
        greeting += "Alien Life from Sector " + str(name)
    return greeting


# No arguments:
print(hello())

# Single argument:
print(hello("Serena"))

# int argument works too:
print(hello(110))
print(hello(3.14))