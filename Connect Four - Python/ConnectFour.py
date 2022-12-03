
gameboard = []
from random import randint, seed 
seed(100)
#Function to create empty game board using dimensions entered by the User
def createGameboard(rowSize,columnSize):
    while(len(gameboard) < rowSize):
        gameboard2 = []
        while(len(gameboard2) < columnSize):
            gameboard2.append('_')
        gameboard.append(gameboard2[:])
#Function to print gameboard
def printGameboard(gameboard):
    row = 0
    while row < len(gameboard):
        col = 0
        while col < len( gameboard[row] ):
            print( gameboard[row][col], end = " ")
            col += 1
        print() 
        row += 1
# Function of gameplay when playing  against human opponent
def humanPlaygame(gameboard,columnSize):
    turn = 0
    tiecount=0
    gameover=False
    while gameover==False:
        if(turn == 0):
            print("Player 1's turn")
            selection = int(input("Enter a column to place your piece in:"))
            while (selection<1) or (selection>columnSize):
                print("Invalid column, please select a column that exists.")
                selection = int(input("Enter a column to place your piece in:"))
            columnfull=presenceCheck(gameboard, selection)
            while columnfull==True:
                selection = int(input("Enter a column to place your piece in:"))
                columnfull=presenceCheck(gameboard, selection)
            row = len(gameboard) - 1
            while (row >= 0):
                if gameboard[row][selection - 1] == '_':
                    gameboard[row][selection - 1] = 'X'
                    row = 0
                row -= 1
            printGameboard(gameboard)
            tiecount= tieCheck(gameboard)
            player1win=Xwincheck(gameboard)
            if player1win > 0:
                print("Player 1 wins!")
                gameover=True
            elif tiecount>0:
                print("Game tied")
                gameover=True
            else:
                turn += 1
                print("Player 2's turn")
                selection = int(input("Enter a column to place your piece in:"))
                while (selection<1) or (selection>columnSize):
                    print("Invalid column, please select a column that exists.")
                    selection = int(input("Enter a column to place your piece in:"))
                columnfull=presenceCheck(gameboard, selection)
                while columnfull==True:
                    selection = int(input("Enter a column to place your piece in:"))
                    columnfull=presenceCheck(gameboard, selection)
                row = len(gameboard) - 1
                while (row >= 0):
                    if gameboard[row][selection - 1] == '_':
                        gameboard[row][selection - 1] = 'O'
                        row = 0
                    row -= 1 
                printGameboard(gameboard)
                player2win = Owincheck(gameboard)
                tiecount=tieCheck(gameboard)
                if player2win>0:
                    print("Player 2 wins!")
                    gameover=True
                elif tiecount>0:
                    print("Game tied")
                    gameover=True
                turn += 1
        turn = turn % 2
#Function to play against computer
def computerPlaygame(gameboard,columnSize):
    turn = 0
    tiecount = 0
    gameover=False
    while gameover==False:
        if(turn == 0):
            print("Player 1's turn")
            selection = int(input("Enter a column to place your piece in:"))
            while (selection<1) or (selection>columnSize):
                print("Invalid column, please select a column that exists.")
                selection = int(input("Enter a column to place your piece in:"))
            row = len(gameboard) - 1
            while (row >= 0):
                if gameboard[row][selection - 1] == '_':
                    gameboard[row][selection - 1] = 'X'
                    row = 0
                row -= 1
            printGameboard(gameboard)
            player1win=Xwincheck(gameboard)
            tiecount= tieCheck(gameboard)
            if player1win > 0:
                print("Player 1 wins!")
                gameover=True
            elif tiecount>0:
                print("Game tied")
                gameover=True
            else:
                turn += 1
                print("It's the Computer's turn")
                selection = randint(1,columnSize)
                while (selection<1) or (selection>columnSize):
                    print("Invalid column, please select a column that exists.")
                    selection = randint(1,columnSize)
                row = len(gameboard) - 1
                while (row >= 0):
                    if gameboard[row][selection - 1] == '_':
                        gameboard[row][selection - 1] = 'O'
                        row = 0
                    row -= 1
                printGameboard(gameboard)
                player2win = Owincheck(gameboard)
                tiecount = tieCheck(gameboard)
                if player2win>0:
                    print("Computer wins!")
                    gameover=True    
                elif tiecount>0:
                    print("Game tied")
                    gameover=True
                turn += 1
            turn = turn % 2
# to check if top row is full
def presenceCheck(gameboard,selection):
    columnfull=False
    if (gameboard[0][selection-1]=="X") or (gameboard[0][selection-1]=="O"):
        print("This column is full.Please select some other column.")
        columnfull=True
    return columnfull
def Owincheck(gameboard):
    Owincounter=0
    gameboardHeight = len(gameboard[0])
    gameboardWidth = len(gameboard)
    tile = 'O'
    # check for horizontal win
    for y in range(gameboardHeight):
        for x in range(gameboardWidth - 3):
            if gameboard[x][y] == tile and gameboard[x+1][y] == tile and gameboard[x+2][y] == tile and gameboard[x+3][y] == tile:
                Owincounter+=1
    # check for vertical win
    for x in range(gameboardWidth):
        for y in range(gameboardHeight - 3):
            if gameboard[x][y] == tile and gameboard[x][y+1] == tile and gameboard[x][y+2] == tile and gameboard[x][y+3] == tile:
                Owincounter+=1
    # check diagonal win
    for x in range(gameboardWidth - 3):
        for y in range(3, gameboardHeight):
            if gameboard[x][y] == tile and gameboard[x+1][y-1] == tile and gameboard[x+2][y-2] == tile and gameboard[x+3][y-3] == tile:
                Owincounter+=1
    
    for x in range(gameboardWidth - 3):
        for y in range(gameboardHeight - 3):
            if gameboard[x][y] == tile and gameboard[x+1][y+1] == tile and gameboard[x+2][y+2] == tile and gameboard[x+3][y+3] == tile:
                Owincounter+=1          
    return Owincounter
def Xwincheck(gameboard):
    Xwincounter=0
    gameboardHeight = len(gameboard[0])
    gameboardWidth = len(gameboard)
    tile = "X"
    # check for horizontal win
    for y in range(gameboardHeight):
        for x in range(gameboardWidth - 3):
            if gameboard[x][y] == tile and gameboard[x+1][y] == tile and gameboard[x+2][y] == tile and gameboard[x+3][y] == tile:
                Xwincounter+=1
    # check for vertical win
    for x in range(gameboardWidth):
        for y in range(gameboardHeight - 3):
            if gameboard[x][y] == tile and gameboard[x][y+1] == tile and gameboard[x][y+2] == tile and gameboard[x][y+3] == tile:
                Xwincounter+=1
    # check diagonal win
    for x in range(gameboardWidth - 3):
        for y in range(3, gameboardHeight):
            if gameboard[x][y] == tile and gameboard[x+1][y-1] == tile and gameboard[x+2][y-2] == tile and gameboard[x+3][y-3] == tile:
                Xwincounter+=1
    for x in range(gameboardWidth - 3):
        for y in range(gameboardHeight - 3):
            if gameboard[x][y] == tile and gameboard[x+1][y+1] == tile and gameboard[x+2][y+2] == tile and gameboard[x+3][y+3] == tile:
                Xwincounter+=1          
    return Xwincounter
# check if board is full
def tieCheck(gameboard):
    count=0
    for t in range(0,len(gameboard)):
        if (gameboard[0][t] == "X") or (gameboard[0][t] == "O"):
            count+=1
    return count    
def main():
    newGame="y"
    print("Welcome to connect4!")
    while newGame=="y":
        columnSize = int(input("Enter a width:"))
        rowSize = int(input("Enter a height:"))
        while (rowSize < 5) or (columnSize < 5):
            print("Both rows and columns must be greater than 5")
            columnSize = int(input("Enter a width: "))
            rowSize = int(input("Enter a height:"))
        createGameboard(rowSize, columnSize) 
        printGameboard(gameboard)
        playmode = input("Do you want to play against the computer?(y or n): ")
        if playmode == "n":
            humanPlaygame(gameboard, columnSize)
        elif playmode == "y":
            computerPlaygame(gameboard, columnSize)
        newGame = input("Do you want to play a new game?")
main()
