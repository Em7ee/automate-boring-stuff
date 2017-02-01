#!/usr/bin/python3.5

# Small program that will keep asking you to type your name with a break.

while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank You!')