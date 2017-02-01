#!/usr/bin/python3.5

# Game to demonstrate the Collatz sequence.
# Made by jan0sik
# Dated June 27, 2016

import sys

def collatz(number):

    if number % 2 == 0:
        result = number // 2
    elif number % 2 == 1:
        result = 3 * number + 1

    while result == 1:
        print(result)
        sys.exit()

    while result != 1:
        print(result)
        number = result
        return collatz(number)

print('Enter number: ')
try:
    number = int(input())
    collatz(number)
except ValueError:
    print('You must enter an integer type.')