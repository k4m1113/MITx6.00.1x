#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 11:11:19 2017

@author: Andromeda
"""
high = 100
low = 0
next_move = ''
print('Please think of a number between 0 and 100!')

while next_move != 'c':
    guess = int((high + low)/2)
    print("Is your secret number " + str(guess) + "?")
    next_move = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if next_move == 'l':
        low = guess
        guess = (high + low)/2

    elif next_move == 'h':
        high = guess
        guess = (high + low)/2
    elif next_move == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')
print('Game over. Your secret number was: ' + str(guess))