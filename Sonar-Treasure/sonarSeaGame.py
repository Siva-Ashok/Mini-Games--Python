#SONAR SEA GAME

import random
import sys
import math

def newBoard():
    board=[]
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0,1)==0:
                board[x].append("~")
            else:
                board[x].append("`")
    return board


def drawBoard(board): 
    fourSpace="    "
    nineSpace="         "
    firstLine=fourSpace+nineSpace
    for i in range(1,6):
        firstLine += str(i)+nineSpace
    print(firstLine)

    threeSpace="   "
    numbers="0123456789"*6
    secondLine=threeSpace+numbers
    print(secondLine)
    print()

    for y in range(15):
        if y<10:
            yAxis=" "+str(y)+" "
        else:
            yAxis=str(y)+" "
        for x in range(60):
            yAxis += board[x][y]
        yAxis += " "+str(y)
        print(yAxis)
    print()
    print(secondLine)
    print(firstLine)


def getRandomChests(numChests):
    chests=[]
    while len(chests)<numChests:
        newChests=[random.randint(0,59),random.randint(0,14)]
        chests.append(newChests)
    return chests

def isBoard(x,y):
    return x>=0 and x<=59 and y>=0 and y<=14

def makeMove(board,chests,x,y):
    smallestDistance=100
    for cx,cy in chests:
        distance=math.sqrt((cx-x)*(cx-x)+(cy-y)*(cy-y))
        if distance<smallestDistance:
            smallestDistance=distance
    if smallestDistance==0:
        board[x][y]="X"  
        chests.remove([x,y])
        return "Chests Found"
        
    else:
        if smallestDistance<10:
            board[x][y]=str(int(smallestDistance))
            return "chests Near"
        else:
            board[x][y]="X"
            return "Out of Range" 
     

def playerMove(previousMoves):
    while True:
        print("Enter the Moves 0 to 59 and 0 to 14..")
        move=input().split()
        if len(move)==2 and move[0].isdigit() and move[1].isdigit and isBoard(int(move[0]),int(move[1])):
            if[int(move[0]),int(move[1])] in previousMoves:
                print("you alreadr moved")
                continue
            return [int(move[0]),int(move[1])]

while True:
    SONAR_DEVISES=20
    numChests=3
    board=newBoard()    
    drawBoard(board)
    theChests=getRandomChests(numChests)
    print(theChests)
    previousMoves=[]

    while SONAR_DEVISES >0:
        x,y = playerMove(previousMoves)
        previousMoves.append([x,y])

        move=makeMove(board,theChests,x,y)
        drawBoard(board)
        print(move)

        if len(theChests)==0:
            print("you won")
            sys.exit

        SONAR_DEVISES -= 1

    if SONAR_DEVISES ==0:
        for x,y in theChests:
            print(" %s,%s"%(x,y))

      

    
        
        
        

                    
