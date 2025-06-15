import random 

print("dice rolling game")
def roll_dice():
    return random.randint(1, 6)
print("Rolling the dice...")
result = roll_dice()
print(f"You rolled a {result}")
