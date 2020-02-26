#!/usr/bin/env python3.8
import re
from random import randint
words = ('apple', 'antelope', 'banana','badger', 'colour','circular', 'dizzy','dither', 'energy','expert', 'flesh','framed', 'grape','giant', 'holiday','hopeful','hymn', 'icicle','irate', 'jazzy','jigsaw', 'knitting','kayaking', 'lumpy','lynx', 'muscle','microwave', 'night','numbskull', 'opened','oxygen','present', 'queen','queue','remove','rhythm','settle','squawk','touch','twelfth','untied','unknown','vases','voodoo','wrench','whiskey','young','yacht','zoomed','zodiac')


def charcheck(strg, search=re.compile(r'[^a-z]').search):
    return not bool(search(strg))

def inputword():
    while True:
        user_word = str((input('Player 1: please enter a word for Player 2 to guess: ')))
        
        if len(user_word) >= 20:
            print('That looks too long, please enter a word of 20 characters or less')
        if len(user_word) <1:
            print("")
        elif charcheck(user_word) == False:
            print('Please only enter lowercase letters')
        else:
            print('\n' * 50)
            return user_word


HANGMANPICS = ['''
  






=========''','''
  
      |
      |
      |
      |
      |
=========''','''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def randomword(wordlist):
    select = wordlist[randint(0,len(words))]
    return select

def display(HANGMANPICS, wrong, correct, hangword):
    print(HANGMANPICS[len(wrong)])

    blanks = '_' * len(hangword)
    for c in range(len(hangword)):
        if hangword[c] in correct:
            blanks = blanks[:c] + hangword[c] + blanks[c+1:]
    
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyguessed):
    while True:
        guess = input('Guess a letter ')
        if len(guess) != 1:
            print('One letter at a time')
        elif guess in alreadyguessed:
            print('You already guessed that!')
        elif charcheck(guess) == False:
            print('Please enter a lowercase l e t t e r, dummy')
        else:
            return guess

def playagain():
    print('Do you want to play another round?')
    return input().lower().startswith('y')

print('''                                                        |/|
 _                                                     (___)           
| |                                                    // \\\\         
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __         //   \\\\         
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \       ||     ||              
| | | | (_| | | | | (_| | | | | | | (_| | | | |      ||     ||      
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|      ||     ||
                    __/ |                             \\\\___//
                   |___/  By Finn Macrae               ----- ''')

wrong = ''
correct = ''
hangword = ''
gameover = False
lives = len(HANGMANPICS)-1

won = False

def twoplayer():
    print('Do you want another player to input a word for you to guess?')
    return input().lower().startswith('y')

if twoplayer():
    hangword = inputword()
else:
    hangword = randomword(words)

while gameover==False:
    display(HANGMANPICS,wrong,correct,hangword)
    print('You have ',lives,' guesses left')
    guess = getGuess(wrong + correct)
    if guess in hangword:
        correct = correct + guess
        won = True
    for c in range(len(hangword)):
        if hangword[c] not in correct:
            won = False
            break
    if won:
        print('You win! The word was '+ hangword.upper()+'!')
        gameover = True
    if guess not in hangword:
        wrong = wrong + guess
        lives = lives - 1
        if len(wrong) == len(HANGMANPICS) - 1:
            display(HANGMANPICS,wrong,correct,hangword)
            print('You have run out of guesses!\nAfter ' + str(len(wrong)) + ' wrong guesses and ' + str(len(correct)) + ' correct guesses, the word was "' + hangword + '"')
            gameover = True

        
    if gameover:
        if playagain():
            wrong= ""
            correct= ""
            gameover = False
            lives = len(HANGMANPICS)-1
            if twoplayer():
                hangword = inputword()
            else:
                hangword = randomword(words)
        else:
            print('Goodbye!')
            break
        

