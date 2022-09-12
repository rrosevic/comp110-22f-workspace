"""Exercise Two - A One Shot Wordle."""
__author__: str = "730575822"

# declaring secret word, guessed word, index, and emoji variables
secret: str = "hello"
wordle_guess: str = input(f"What is your {len(secret)}-letter guess? ")


while len(wordle_guess) != len(secret):
    wordle_guess = input(f"That was not {len(secret)} letters! Try again: ")

wordle_index: int = 0
emoji_result: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# runs the game when player's guess has fewer characters than the index of the secret word
while wordle_index < len(secret):
    if wordle_guess[wordle_index] == secret[wordle_index]:
        emoji_result += GREEN_BOX
    else:  # runs if a character is not correct and in the right spot (otherwise a green emoji prints)
        chr_guess: bool = False
        alt_indicies: int = 0
        while chr_guess == False and alt_indicies < len(secret):  # runs until all characters of secret and guess are compared
            if secret[alt_indicies] == wordle_guess[wordle_index]:
                chr_guess = True 
            else:
                alt_indicies += 1
        if chr_guess == True:  # only true if any secret characters align with current guess character. results in yellow block emoji
            emoji_result += YELLOW_BOX
        else:  # guessed character is not in the secret. results in a white block emoji.
            emoji_result += WHITE_BOX
    wordle_index += 1  # avoid endless loop and run through next character of the guessed wordle's index

print(emoji_result)
# here's how you did! :) with emojis, colors, and verbal feedback
if wordle_guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")