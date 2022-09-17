"""Examples of using lists in a simple 'game'."""

from random import randint
rolls: list[int] = list()  

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1,6))

print(rolls)

#Remove an item from the lsit by its index ("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# Sum the values of our rolls!
i: int = 0
sum: int = 0
while 1 < len(rolls):
    sum = sum + rolls[i]
    i = i + 1
print(f"Total score: {sum}")


# rolls.append(randint(1,6))
# rolls.append(randint(1,6))
# rolls.append(randint(1,6))
# print(rolls)

# # Access an individual item
# print(rolls[0])
# print(rolls[1])

# # Access the lenght of a list (number of items)
# print(len(rolls))

# #Access the last item of a list
# last_index: int = len(rolls) - 1
# print(rolls[last_index]) 