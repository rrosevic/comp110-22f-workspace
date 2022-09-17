"""An example of a list utility algorithm."""

# Name: contains
# Function with two parameters
#  needle - what we're searching for
#  haystack - what we're searching through
#  Return type: bool
def contains(needle: str, haystack: str) -> bool:
# Start from first index
    i: int = 0
    # Loop through each index of list
    while i < len(haystack):
        # Test if equal to needle
        if haystack[i] == needle:
            # if yes, return True!
            return True
        i += 1 
    # otherwise return False
    return False
