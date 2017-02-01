#!/usr/bin/python3.5

# This is a geuss the number game.
# Create by jan0sik

import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player the guess 6 times
for guessesTaken in range(1, 7):
    print('Take a geuss.')
    guess = int(input())

    if guess < secretNumber:
        print('Your geuss is too low.')
    elif guess > secretNumber:
        print('Your geuss is too high.')
    else:
        break   # This condition is the correct guess, or you are out of guesses!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
