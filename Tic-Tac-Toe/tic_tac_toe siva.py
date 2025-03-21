#Tic Tac Toe


import random


def displayBoard(board):
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("-+-+-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-+-+-")
    print(board[1]+"|"+board[2]+"|"+board[3])
    print()
    
    
def getplayerLetter():
    playerLetter=" "
    while playerLetter not in "XO":
        print("Enter the player Letter X or O...")
        playerLetter=input().upper()
    if playerLetter=="X":
        return ["X","O"]
    else:
        return ["o","x"]
    
    
def firstMove():
    firstMove=random.choice(["computer","player"])
    if firstMove=="player":
        return "computer"
    else:
        return "player"

def makeMove(board,letter,move):
    board[move]=letter


def isWon(board,letter):
    return((board[7]==letter and board[8]==letter and board[9]==letter)or
           (board[4]==letter and board[5]==letter and board[6]==letter)or
           (board[1]==letter and board[2]==letter and board[3]==letter)or
           (board[7]==letter and board[4]==letter and board[1]==letter)or
           (board[8]==letter and board[5]==letter and board[2]==letter)or
           (board[9]==letter and board[6]==letter and board[3]==letter)or
           (board[7]==letter and board[5]==letter and board[3]==letter)or
           (board[9]==letter and board[5]==letter and board[1]==letter))


def spaceAvailable(board,move):
    return board[move]==' '


def playerMove(board):
    playerMove=" "
    while playerMove not in "1 2 3  4 5 6 7 8 9".split() or not spaceAvailable(board,int(move)):
        print("Enter the valid Position....")
        playerMove=input()
        return int(playerMove)

def getBoardCopy(board):
    boardCopy=[]
    for i in board:
        boardCopy.append(i)
    return boardCopy

def computerMove(board,computerLetter):
    for i in range(1,len(board)):
        boardCopy=getBoardCopy(board)
        if spaceAvailable(boardCopy,i):
            makeMove(boardCopy,computerLetter,i)
            if isWon(boardCopy,computerLetter):
                return i

    for i in range(1,len(board)):
        boardCopy=getBoardCopy(board)
        if spaceAvailable(boardCopy,i):
            makeMove(boardCopy,playerLetter,i)
            if isWon(boardCopy,playerLetter):
                return i

                
    boardCopy=getBoardCopy(board)
    possibleMoves=[]
    possibleCorners = ["1", "3", "7", "9"]
    for i in possibleCorners:
        if spaceAvailable(boardCopy,int(i)):
            possibleMoves.append(int(i))
    if possibleMoves:
        return random.choice(possibleMoves)

    if spaceAvailable(board,5):
        return 5

    
    possibleSides = ["2", "4", "6", "8"]
    for i in possibleSides:
        if spaceAvailable(boardCopy,int(i)):
            possibleMoves.append(int(i))
    if possibleMoves:
        return random.choice(possibleMoves)


def isBoardFull(board):
    for i in range(1,len(board)):
        if spaceAvailable(board,i):
            return False
    return True


print("Welcome To Tic-Tac-Toe....")
board=[" "]*10
playerLetter,computerLetter=getplayerLetter()
getFirstMove=firstMove()
gameplay=True
print("The First Move On:"+getFirstMove)

while gameplay:
    
    if getFirstMove=="player":
        displayBoard(board)
        move= playerMove(board)
        makeMove(board,playerLetter,move)
        if isWon(board,playerLetter):
            displayBoard(board)
            print("player Won")
            gameplay=False
        else:
            if isBoardFull(board):
                displayBoard(board)
                print("Game is tie...")
                gameplay=False

            else:
                getFirstMove="computer"

    else:
        
        move=computerMove(board,computerLetter)
        makeMove(board,computerLetter,move)
        if isWon(board,computerLetter):
            displayBoard(board)
            print("Computer  Won")
            gameplay=False
        else:
            if isBoardFull(board):
                displayBoard(board)
                print("Game is tie...")
                gameplay=False
            else:
                getFirstMove="player"


                

            
    
        
        


    

















