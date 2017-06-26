#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 15:17:15 2017

@author: Andromeda
"""

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guessesAvailable = 8
    lettersGuessed = []
    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
    test = getGuessedWord(secretWord, lettersGuessed)
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long')
    while '_' in test:
        print('-------------')
        if guessesAvailable > 0: 
            print('You have ' + str(guessesAvailable) + ' guesses left.')
            print('Available letters: ' + getAvailableLetters(lettersGuessed))
            guess = input('Please guess a letter: ').lower()
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter: " + test)
            else:
                lettersGuessed.append(guess)
                test = getGuessedWord(secretWord, lettersGuessed)
                if guess in secretWord:
                    print('Good guess: ' + test)
                else:
                    print('Oops! That letter is not in my word: ' + test)
                    guessesAvailable -= 1
        else:
            print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
            break
    if '_' not in test:
        print('-------------')
        print('Congratulations, you won!')

    