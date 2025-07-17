logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
import random

print(logo)
print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

lives = 0

while difficulty != "easy" and difficulty != "hard":
    print("Invalid difficulty")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5

print(f"You have {lives} attempts remaining to guess the number.")
guess = int(input("Make a guess: "))

number = random.randint(1,100)

while guess != number and lives > 0:
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    print("Guess again.")
    lives -= 1
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

if lives == 0 and guess != number:
    print("You've run out of guesses. Refresh the page to run again.")
elif lives > 0 and guess == number:
    print(f"You got it! The answer was {number}.")

