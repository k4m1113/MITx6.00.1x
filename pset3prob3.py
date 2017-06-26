#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 15:13:44 2017

@author: Andromeda
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
    for letter in lettersGuessed:
        alphabet.remove(letter)
    return ''.join(alphabet)