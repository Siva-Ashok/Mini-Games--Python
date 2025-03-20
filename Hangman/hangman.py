
#HANGMAN PROGRAM

import random

HANGMAN_PICS=['''
  *---+
      |
      |
      |
     ===''','''
  +---+
  0   |
      |
      |
     ===''','''
  +---+
  0   |
  |   |
      |
     ===''','''
  +---+
  0   |
 /|   |
      |
     ===''','''
  +---+
  0   |
 /|\  |
      |
     ===''','''
  +---+
  0   |
 /|\  |
 /    |
     ===''','''
  +---+
  0   |
 /|\  |
 / \  |
     ===''']

words='''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''
wordList=words.split()

def randomWord(wordList):
    randomIndex=random.randint(0,len(wordList)-1)
    return wordList[randomIndex]

def getGuess(alreadyGuessed):
    while True:
        print("guess a letter")
        guess=input()
        if len(guess) !=1:
            print("enter a single letter")
        elif guess in alreadyGuessed:
            print("enter the letter already guessed")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print(" please enter a letter")
        else:
            return guess
 
def playAgain():
    print("Do you want to playAgain? (yes or no)... ")
    return input().lower().startswith("y")
    
def displayBoard(missedLetters,correctLetters,secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("missedLetters:",end='')
    for letter in missedLetters:
          print(letter,end=' ')
    print()

    blanks= "_"*len(secretWord)
    
    for i in range(len(secretWord)):
          if secretWord[i] in correctLetters:
              blanks=blanks[:i]+secretWord[i]+blanks[i+1:]

    for letter in blanks:
        print(letter,end=' ')
    print()

isFreshGame = True
while isFreshGame:
    print("H A N G M A N")
    missedLetters=''
    correctLetters=''
    secretWord=randomWord(wordList)
    gameDone=False  
    while True:
        displayBoard(missedLetters,correctLetters,secretWord)
        guess=getGuess(missedLetters+correctLetters)
        if guess in secretWord:
            correctLetters=correctLetters+guess
            foundAllLetters=True
            for i in range (len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters=False
                    break
            if foundAllLetters:
                print("you Won")
                gameDone=True
        else:
            missedLetters=missedLetters+guess
            if len(missedLetters)==len(HANGMAN_PICS)-1:
                displayBoard(missedLetters, correctLetters, secretWord) 
                print("you Lose,The secret Word is:"+secretWord)
                break
    if not playAgain():
        isFreshGame = False
        



            
    
       
   
        


        
    
        

