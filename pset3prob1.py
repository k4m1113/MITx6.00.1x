#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 15:01:33 2017

@author: Andromeda
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    test = secretWord[:]
    for letter in lettersGuessed:
        test = test.replace(letter, '')
    if len(test) == 0:
        ans = True
    else:
        ans = False
    return ans