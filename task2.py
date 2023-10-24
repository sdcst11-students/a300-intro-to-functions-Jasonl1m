"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random
def game():
    for i in range(10):
        x = input("Guess a number = ")
        y = random.randint(1,100)
        if x == y:
            print("You are correct!")
            break
        elif i == 9:
            print("You have lost :(")
            break
        else:
            print("You are incorrect!")


def title():
    print("You have 10 tries to enter a number between 1 and 100, if you guess correct you win! Good luck!")
title()