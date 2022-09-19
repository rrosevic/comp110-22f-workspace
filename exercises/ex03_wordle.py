"""Exercise 3 - A Structured Wordle."""
__author__ = "730575822"


def contains_char(wordle_guess: str, wordle_char: str) -> bool:
    """Checks all characters of player's guess to find matches in the wordle."""
    assert len(wordle_char) == 1
    i: int = 0
    while i < len(wordle_guess):
        if wordle_guess[i] == wordle_char:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Uses character matching from contains_char to call for a white or yellow emoji."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    emoji: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX 
        i += 1
    return emoji


def input_guess(guess_length: int) -> str:
    """Prompts the user for a guess until the expected length is given."""
    user_guess: str = input(f"Enter a {guess_length} character word: ")
    while len(user_guess) != guess_length:
        user_guess = input(f"That wasn't {guess_length} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "frame"
    user_turns: int = 1
    user_win: bool = False
    while user_turns < 7 and user_win is False:
        print(f"=== Turn {user_turns}/6 ===")
        user_guess: str = input_guess(len(secret))
        print(emojified(user_guess, secret))
        if user_guess == secret: 
            user_win = True
        else:
            user_turns += 1
    if user_win is True:
        print(f"You won in {user_turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()