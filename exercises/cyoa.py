"""Exercise 6 - Choose Your Own Adventure: What plant or fruit are you most like?"""
__author__: str = "730575822"

points: int = 0
player: str = ""

SMILEY_FACE: str = "\U0001F60A"
HEART_EMOJI: str = "\U0001F90D"
PLANT_EMOJI: str = "\U0001FAB4"
CACTUS_EMOJI: str = "\U0001F335"
LEMON_EMOJI: str = "\U0001F34B"
PLANT_BULLET: str = "\U0001F331"
FRUIT_BULLET: str = "\U0001F353"
HERB_EMOJI: str = "\U0001F33F"
EVERGREEN: str = "\U0001F332"
CLOVER_EMOJI: str = "\U0001F340"
APPLE_EMOJI: str = "\U0001F34E"
PINEAPPLE: str = "\U0001F34D"
AVOCADO_EMOJI: str = "\U0001F951"


def main() -> None:
    """Entrypoint of quiz game."""
    greet()
    global player
    global points
    print(f"\nAlright, {player}, choose what you'd like to do next:")
    choice: str = input("1: Stop Playing \n2: What plant am I most like? \n3: What fruit am I most like? \nInput choice here: ")
    user_choice: int = int(choice)
    if user_choice == 1:
        end_game()
    elif user_choice == 2:
        plant_quiz()
        pscore: int = plant_score(points)
        points += pscore
        if pscore == 2:
            post_eval()
    else:
        fruit_quiz()
        fscore_results: int = fruit_score(points)
        points += fscore_results
        if fscore_results == 2:
            post_eval()

    game_loop()


def greet() -> None:
    """A welcome message for the player."""
    print("Hello there! Welcome to the quiz!")
    input(f"The quizzes you are about to take will show you what plant or fruit you are most like (press Enter to continue){PLANT_EMOJI}  ")
    input("Either quiz will consist of four questions about yourself, each with three answer choices.")
    input("Choose answers that best describe you.")
    global player
    player = input("Let's get started! What is your name? ")


def end_game() -> None:
    """The user chooses to end the game before it begins."""
    global points
    print(f"\nYou chose to end the game. \nAdventure Points: {points}")
    print("You are most like...")
    input(f"a cactus{CACTUS_EMOJI}  and a lemon{LEMON_EMOJI} !  sour, prickly, and rude. Play sometime soon. \n(press Enter)")


def plant_quiz() -> None:
    """A questionarre to identify the plant you are most like."""
    input(f"\nYay, {player}! you chose to continue to the plant quiz!{SMILEY_FACE} ")
    global points
    print(f"{PLANT_BULLET}  What statement would your friends describe you with?")
    print("1: A nurturing friend who supports you through everything. \n2: Will tell you what you need to hear, even if it hurts. \n3: Turns every situation into a lucky one.")
    first_question: str = input("Answer choice here: ")
    points += int(first_question)

    print(f"\n{PLANT_BULLET}  What would your teachers say you are most like?")
    print("1: Will be partners with anyone, no questions asked. \n2: Studies hard and pushes their friends to succeed. \n3: Aces every exam even though they don't study.")
    second_question: str = input("Answer choice here: ")
    points += int(second_question)

    print(f"\n{PLANT_BULLET}  How do you view yourself?")
    print("1: I think I'm pretty friendly! \n2: I might seem mean, but I'm actually really soft-hearted. \n3: I'm a very lucky person no matter where I go.")
    third_question: str = input("Answer choice here: ")
    points += int(third_question)

    from random import randint
    random_number: int = randint(1, 2)
    if random_number == 1:
        print(f"\n{PLANT_BULLET}  What is your ideal social setting?")
        print("1: I like to spend meaningful, one-on-one time with my friends and family. \n2: I go out a lot, but my favorite thing to do is stay home alone. \n3: I go wherever life takes me!")
        fourth_question_a: str = input("Answer choice here: ")
        points += int(fourth_question_a)
    else:
        print(f"\n{PLANT_BULLET}  Where do you feel most at home?")
        print("1: Anywhere I am helping someone else. \n2: I like being with my friends, but honestly prefer my own company. \n3: I create home wherever I am.")
        fourth_question_b: str = input("Answer choice here: ")
        points += int(fourth_question_b)


def plant_score(player_points: int) -> int:
    """A player's final score."""
    score: int = 0
    if player_points > 0 and player_points <= 4:
        score = 1
    if player_points > 4 and player_points <= 8:
        score = 2
    if player_points > 8 and player_points <= 12:
        score = 3
    your_plant(score)
    print("\nDo you think this is accurate? \n1: Almost! \n2: No, not really... \n3: Absolutely.")
    final_question: int = int(input("Answer choice here: "))
    if final_question == 1:
        print("That's good to hear!")
    if final_question == 2:
        print("We're sorry. Your score has been updated. Would you like to see if your results have changed?")
    if final_question == 3:
        print("That's fantastic!")
    return final_question
    

def your_plant(results: int) -> str:
    """Tells you your soul plant based on score from questionarre."""
    herb: str = f"You are most like a healing herb plant! {HERB_EMOJI} \nYou are kind, compassionate, and caring. Use your strengths to share \nlove with the world (don't forget to take care of yourself, too {HEART_EMOJI}\n)"
    evergreen: str = f"You are most like an evergreen tree! {EVERGREEN} \nYou stand tall and strong year-round, and always make sure your friends \ndo, too (don't forget about your personal agency {HEART_EMOJI}\n)"
    clover: str = f"You are most like a four-leaf clover! {CLOVER_EMOJI} \nYou are very lucky, no matter what your outward circumstances are like. \nYou've createdyour own luck and it just keeps coming! Give yourself credit for that {HEART_EMOJI}\n"
    if results == 1:
        print(herb)
    if results == 2:
        print(evergreen)
    if results == 3:
        print(clover)


def fruit_quiz() -> None:
    """A questionarre to identify the fruit you are most like."""
    input(f"\nYay, {player}! you chose to continue to the fruit quiz!{SMILEY_FACE} ")
    global points
    print(f"{FRUIT_BULLET}  What statement would your friends describe you with?")
    print("1: A nurturing friend who supports you through everything. \n2: Will tell you what you need to hear, even if it hurts. \n3: Turns every situation into a lucky one.")
    first_question: str = input("Answer choice here: ")

    points += int(first_question)    
    print(f"\n{FRUIT_BULLET}  What would your teachers say you are most like?")
    print("1: Will be partners with anyone, no questions asked. \n2: Studies hard and pushes their friends to succeed. \n3: Aces every exam even though they don't study.")
    second_question: str = input("Answer choice here: ")
    points += int(second_question)

    print(f"\n{FRUIT_BULLET}  How do you view yourself?")
    print("1: I think I'm pretty friendly! \n2: I might seem mean, but I'm actually really soft-hearted. \n3: I'm a very lucky person no matter where I go.")
    third_question: str = input("Answer choice here: ")
    points += int(third_question)

    from random import randint
    random_number: int = randint(1, 2)
    if random_number == 1:
        print(f"\n{FRUIT_BULLET}  What is your ideal social setting?")
        print("1: I like to spend meaningful, one-on-one time with my friends and family. \n2: I go out a lot, but my favorite thing to do is stay home alone. \n3: I go wherever life takes me!")
        fourth_question_a: str = input("Answer choice here: ")
        points += int(fourth_question_a)
    else:
        print(f"\n{FRUIT_BULLET}  Where do you feel most at home?")
        print("1: Anywhere I am helping someone else. \n2: I like being with my friends, but honestly prefer my own company. \n3: I create home wherever I am.")
        fourth_question_b: str = input("Answer choice here: ")
        points += int(fourth_question_b)


def fruit_score(player_points: int) -> int:
    """A player's final score."""
    score: int = 0
    if player_points > 0 and player_points <= 4:
        score = 1
    if player_points > 4 and player_points <= 8:
        score = 2
    if player_points > 8 and player_points <= 12:
        score = 3
    your_fruit(score)
    print("\nDo you think this is accurate? \n1: Almost! \n2: No, not really... \n3: Absolutely.")
    final_question: int = int(input("Answer choice here: "))
    if final_question == 1:
        print("That's good to hear!")
    if final_question == 2:
        print("We're sorry. Your score has been updated. Would you like to see if your results have changed?")
    if final_question == 3:
        print("That's fantastic!")
    return final_question
    

def your_fruit(results: int) -> str:
    """Tells you your soul fruit based on score from questionarre."""
    print(f"\nYour final score is: {points}")
    apple: str = f"You are most like an apple! {APPLE_EMOJI} \nApples are known to have healing properties in the same way you heal others. \nUse your strengths to share love with the world (don't forget to take care of yourself, too {HEART_EMOJI}\n)"
    pineapple: str = f"You are most like a pineapple! {PINEAPPLE} \nYou stand tall and strong in any environment. You may seem intimidating, \nbut you are just protective of your friends and family and are very sweet on the inside{HEART_EMOJI}\n"
    avocado: str = f"You are most like an avocado! {AVOCADO_EMOJI} \nAvocados are known to carry good luck, just like you! No matter what your \noutward circumstances are like, your luck just keeps coming. Give yourself credit for that{HEART_EMOJI}\n"
    if results == 1:
        print(apple)
    if results == 2:
        print(pineapple)
    if results == 3:
        print(avocado)


def fpost_eval() -> None:
    """If player thinks results are inaccurate, gives them a new score."""
    from random import randint
    print("1: Yes \n2: No")
    new_results: int = int(input("Answer choice here: "))
    if new_results == 1:
        your_fruit(randint(1, 3))
    if new_results == 2:
        print("Okay.")


def game_loop() -> None:
    """User can choose what to do next."""
    print(f"\nWhat would you like to do next, {player}?")
    print("1: Start Over \n2: Plant Quiz \n3: Fruit Quiz")
    next_move: int = int(input("Answer choice here: "))
    if next_move == 1:
        main()
    if next_move == 2:        
        plant_quiz()
        plant_score(points)
        your_plant(plant_score)
        game_loop()
    else:
        fruit_quiz()
        print(f"Your final score is: {points}")
        fruit_score(points)
        your_fruit(fruit_score)
        game_loop()


if __name__ == "__main__":
    main()