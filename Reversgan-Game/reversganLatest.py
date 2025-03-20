import random
import sys

HEIGHT=8
WIDTH=8

def drawBoard():
    board=[]
    for i in range(WIDTH):
        board.append([' ',' ',' ',' ',' ',' ',' ',' '])
    return board


def getNewBoard(board):
    print("  12345678")
    print(" +--------+")
    for x in range(WIDTH):
        print("%s|"%(x+1),end='')
        for y in range(HEIGHT):
            print(board[y][x],end='')
        print("|%s"%(x+1))
    print(" +--------+")
    print("  12345678")
    

def playerTile():
    playerCoin=" "
    while playerCoin not in "XO":
        print("Enter the Player Coin X or O....")
        playerCoin=input().upper()
    if playerCoin =="X":
        return ["X","O"]
    else:
        return ["O","x"]
    

def getFirstMove():
    if random.randint(0,1)== 0:
        return "player"
    else:
        return "computer"
    

def isOnBoard(x,y):
    return x>=0 and x<=WIDTH-1 and y>=0 and y<=HEIGHT-1


def isValidMove(board,tile,xStart,yStart):
    if board[xStart][yStart] != " " or not isOnBoard(xStart,yStart):
        return False

    if tile =="X":
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip=[]
    for xDirection,yDirection in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
        x,y= xStart,yStart
        x += xDirection
        y += yDirection
        while isOnBoard(x,y) and board[x][y]==otherTile:
            x += xDirection
            y += yDirection
            if isOnBoard(x,y) and board[x][y]==tile:
                while True:
                    x -=xDirection
                    y -=yDirection
                    if x==xStart and y==yStart:
                        break
                    tilesToFlip.append([x,y])

    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip


def getValidMoves(board,playerTile):
    validMoves=[]
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board,playerTile,x,y):
                validMoves.append([x,y])
    return validMoves


def getBoardCopy(board):
    boardCopy=drawBoard()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y]=board[x][y]
    return boardCopy


def boardHints(board,tile):
    hintsBoard=getBoardCopy(board)
    for x,y in getValidMoves(board,tile):
        hintsBoard[x][y]="."
    return hintsBoard


def makeMove(board,tile,xStart,yStart):
    tilesToFlip=isValidMove(board,tile,xStart,yStart)
    if tilesToFlip==False:
        return False

    board[xStart][yStart]=tile
    for x,y in tilesToFlip:
        board[x][y]=tile
    return True


def playerMove(board,playerTile):
    print("Enter the hints to the showHints and quit to the exitgame..")
    while True:
        move=input().lower()
        if move=="hints":
            hintsBoard=boardHints(board,playerTile)
            getNewBoard(hintsBoard)
            continue
        elif move=="quit":
            sys.exit()
        else:
            move=move.split()
            if len(move)==2 and move[0].isdigit() and move[1].isdigit():
                x=int(move[0])-1
                y=int(move[1])-1
                if isValidMove(board,playerTile,x,y)==False:
                    print("Enter the Valid Move...")
                    continue
                else:
                    break
            else:
                print("Enter the Valid Move...")
    return [x,y]


def isOnCorner(x,y):
    return (x==0 or x==WIDTH-1) and (y==0 or y==HEIGHT-1)

def score(board):
    xscore= 0
    oscore= 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y]== "X":
                xscore += 1
            elif board[x][y]=="O":
                oscore += 1
    return {"X":xscore,"O":oscore}


def printScore(board, playerTile, computerTile):
    scores = score(board)
    print('player letter %s: %s points. Computer letter %s: %s points.' % (playerTile,scores[playerTile],computerTile,scores[computerTile]))

    
def computerMove(board,computerTile):
    possibleMoves=getValidMoves(board,computerTile)
    random.shuffle(possibleMoves)

    # 1)Algoritham in possible Cornes
    for  x,y in possibleMoves:
        if isOnCorner(x,y):
            return [x,y]

    # 2)Algoritham in best Score
    bestScore = -1
    for x,y in possibleMoves:
         boardCopy=getBoardCopy(board)
         makeMove(boardCopy,computerTile,x,y)
         scores=score(boardCopy)
         if scores[computerTile] > bestScore:
             bestMove=[x,y]
             bestScore=scores[computerTile]
    return bestMove

    
def playGame(playerTile,computerTile):
    board=drawBoard()
    board[3][3]="X"
    board[3][4]="O"
    board[4][3]="O"
    board[4][4]="X"
    turn=getFirstMove()
    print("The First Move On:",turn)

    while True:
        if turn=="player":
            playerValidMoves=getValidMoves(board,playerTile)
            if playerValidMoves==[]:
                return board
            else:
                move=playerMove(board,playerTile)
                makeMove(board,playerTile,move[0],move[1])
                getNewBoard(board)
                print(printScore(board, playerTile, computerTile))
            turn="computer"
        else:
            computerValidMoves=getValidMoves(board,computerTile)
            if computerValidMoves==[]:
                return board
            else:
                input("press Enter to see the Computer Move..")
                move=computerMove(board,computerTile)
                makeMove(board,computerTile,move[0],move[1])
                getNewBoard(board)
                print(printScore(board, playerTile, computerTile))
            turn="player"

print("Welcome to ReversGan")

playerTile,computerTile=playerTile()

while True:
    finalBoard=playGame(playerTile,computerTile)
    getNewBoard(finalBoard)
    scores=scorePoints(finalBoard)

    if  scores[playerTile]>scores[computerTile]:
        print("Player Won.Congratulations")
    elif scores[playerTile]<scores[computerTile]:
        print("computer Won The Game")
    else:
        print(" Game is Tie")


    print("Do you Want PlayAgain?")
    if not input().lower().startswith("Y"):
        break
    





