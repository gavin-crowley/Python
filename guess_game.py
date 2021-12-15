import random

number = random.randint(0,100)
# number = 3

print("\nWelcome contestant!")

while number:
    guess = int(input("\nTake a guess what I'm thinking... Any number between 0 and 100: "))
    if guess < number:
        print("Not quite. I'm thinking of a number that is higher.")
    elif guess > number:
        print("Not quite. I'm thinking of a number that is lower.")
    elif guess==number:
        print(f"Well done!!! You guessed right. I was thinking of {number}.")
        print("\nThanks for playing.")
        break



