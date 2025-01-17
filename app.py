#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# ============================================================== #

# Imports a library for generate a random number between 1 and 3, and a library for cleaning the console screen
import random
import os

random_number = random.randint(1, 3)

play=True;


# Generate a block which validates the user input (it must be 'rock', 'paper' or 'scissors') and assigns a number to each option
while play:

    print("Welcome to the game!")
    random_number = random.randint(1, 3)
    user_input = input("Choose your weapon: ")
    # Refactor the following code to use a try/except block to handle the exception

    try:
        if user_input in ["rock", "paper", "scissors"]:
            if user_input == "rock":
                user_number = 1
            elif user_input == "paper":
                user_number = 2
            else: 
                user_number = 3
    except:
        print("Invalid input. Try again!")

    # Generate a block which compares the user input with the random number generated by the computer and determines the winner
    if user_number == random_number:
        print("It's a tie!")
    elif user_number == 1 and random_number == 2:
        print("You lose!")
    elif user_number == 1 and random_number == 3:
        print("You win!")
    elif user_number == 2 and random_number == 1:
        print("You win!")
    elif user_number == 2 and random_number == 3:
        print("You lose!")
    elif user_number == 3 and random_number == 1:
        print("You lose!")
    elif user_number == 3 and random_number == 2:
        print("You win!")
    # Generate a block which asks the user if he/she wants to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "y":
        play=True;
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        play=False;
        print("Thanks for playing!")

