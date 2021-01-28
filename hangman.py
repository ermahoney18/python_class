
import random #for the random.choice function
from re import sub
import numpy as np
import os

hangman_graphics=['''
                  -----------
                  |
                  |
                  |
                  |
                  |
                  |         
               ======''','''
                  -----------
                  |         |
                  |
                  |
                  |
                  |
                  |          
               ======''','''
                  -----------
                  |         |
                  |         O
                  |
                  |
                  |
                  |           
               ======''','''
                  -----------
                  |         |
                  |         O
                  |        /
                  |
                  |
                  |           
               ======''','''
                  -----------
                  |         |
                  |         O
                  |        /|
                  |
                  |
                  |           
               ======''','''
                  -----------
                  |         |
                  |         O
                  |        /|\\
                  |
                  |
                  |           
               ======''','''
                  -----------
                  |         |
                  |         O
                  |        /|\\
                  |         |
                  |
                  |           
               ======''','''
                  -----------
                  |         |
                  |         O
                  |        /|\\
                  |         |
                  |        /
                  |           
               ======''','''
                  -----------
                  |         |
                  |         O
                  |        /|\\
                  |         |
                  |        / \\
                  |          
               ======''']


def read_word_options(filename):
    #read in words
    f = open(filename, 'r')
    word_options = f.readlines()
    f.close()

    #strip newline
    word_options_final = []
    for element in word_options:
        word_options_final.append(element.strip())
    return(word_options_final)

def get_word():
    #choose a word
    word = random.choice(word_options_final)

#prompt for guesses
word = ["example"]

def get_guesses(word):

    print("The word is", len(word[0]), "letters long. Good luck!")
    current = str('_ ' * len(word[0]))
    
    guesses = 0
    guessed = ''
    
    while guesses<8:
        
        #print the hangman graphic appropriate to the moment
        print(hangman_graphics[guesses])

        #take input
        x = input("Guess a letter: ")
        print(current)

        #check if the letter has been guessed
        if(x in guessed):
            print("You already guessed that letter! Try again.")
        elif(x in word[0]):
            print("The letter is in the word!")
            guessed = guessed+x[0]
            current = str(''.join(c if c in guessed else '_ ' for c in word[0]))
            #print(current)
            if(current == word[0]):
                print("Congratulations! You guessed the word:", word[0], "!")
                break
            
        else:
            guesses=guesses+1
            guessed = guessed+x[0]
            print("Guess again: " ,''.join(c if c in guessed else '_ ' for c in word[0]))

        if guesses==8:
            print(hangman_graphics[guesses])
            print("You failed! The word was:" , word[0])
            

#word_options = read_word_options("hangman_words.txt")
#word = get_word(word_options_final)
get_guesses(word)

#now tell it to keep looking until it finishes the word
