#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import *

def random_number():
    return random.randint(1, 100)

def number_guess():
    print(text2art("GuessTheNumber"))
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    gussed_number = random_number()
    print(f"Pssst, the correct answer is {gussed_number}")
    user_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if user_input == "easy":
        attempt = 10
    elif user_input == "hard":
        attempt = 5
    
    while attempt != 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        user_gussed = int(input("Make a guess: "))
    
        if user_gussed == gussed_number:
            print("You got it! The answer was {user_gussed}.")
        elif user_gussed > gussed_number:
            print("Too high.")
            print("Guess again.")
            attempt -= 1
        elif user_gussed < gussed_number:
            print("Too low.")
            print("Guess again.")
            attempt -= 1
    print("You've run out of guesses, you lose.")
number_guess()