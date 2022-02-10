border = "#"
tile = "."
boardMine = "*"

def prettyPrintBoard(board):

    print() # empty line

    # if enough columns, print a "tens column" line above
    if len(board[0])-2 >= 10:
        print("{:25s}".format(""), end="")  # empty space for 1 - 9
        for i in range(10, len(board[0])-1 ):
            print( str(i // 10), end =" ")
        print()

    # create and print top numbered line
    print("       ", end="")
    # only go from 1 to len - 1, so we don't number the borders
    for i in range(1, len(board[0])-1 ):
        # only print the last digit (so 15 --> 5)
        print(str(i % 10), end = " ")
    print()

    # create the border row
    borderRow = "     "
    for col in range(len(board[0])):
        borderRow += board[0][col] + " "

    # print the top border row
    print(borderRow)

    # print all the interior rows
    for row in range(1, len(board) - 1):
        # print the row label
        print("{:3d}  ".format(row), end="")

        # print the row contents
        for col in range(len(board[row])):
            print(str(board[row][col]), end = " ")
        print()

    # print the bottom border row and an empty line
    print(borderRow, "\n")

def createBoard(board):
    userBoard = []
    for col in range( len(board) ):
        row = []
        for gameRow in range( (len(board[col])-1) ):
            if board[col][gameRow] == border:
                row.append(border)
            else:
                row.append(tile)
        userBoard.append(row)
    return userBoard

def numMines(board,gameBoard):
    minesLeft = 0
    row = 0
    while row < len(board):
        col = 0
        while col < len( board[row] ):
            if board[row][col] == boardMine:
                minesLeft += 1
            col += 1
        row += 1
    gbRow = 0
    while gbRow < len(gameBoard):
        gbCol = 0
        while gbCol < len( gameBoard[gbRow] ):
            if gameBoard[gbRow][gbCol] == "f":
                minesLeft -= 1
            gbCol += 1
        gbRow += 1
    print("You have", minesLeft, "mines remaining")

def getchoice(board):
    choices = []
    row = len(board) - 2
    column = len(board[0]) - 2
    print("Please choose the row:")
    rowChoice = int(input("Enter a number between 1 and "+ str(row) +"(inclusive): "))
    while rowChoice < 1 or rowChoice > row :
        print("That number is not allowed.  Please try again!")
        rowChoice = int(input("Enter a number between 1 and "+ str(row) +"(inclusive): "))
    print("Please choose the column:")
    colChoice = int(input("Enter a number between 1 and "+ str(column) +"(inclusive): "))
    while colChoice < 1 or colChoice > column :
        print("That number is not allowed.  Please try again!")
        colChoice = int(input("Enter a number between 1 and "+ str(column) +"(inclusive): "))
    move = input("Enter 'r' to reveal the space,or  \nEnter 'f' to mark the space with a flag:")
    while move != "r" and move != "f":
        print("That's not a valid action")
        move = input("Enter 'r' to reveal the space,or  \nEnter 'f' to mark the space with a flag:")
    choices.append(rowChoice)
    choices.append(colChoice)
    choices.append(move)
    return choices

def neighborNum(board, row, column):
    minecounter = 0
    boardWidth = len(board)
    boardHeight = len(board[0])
    mine ="*"
    if board[row+1][column] == mine:
        minecounter += 1
    if board[row-1][column] == mine:
        minecounter += 1
    if board[row][column-1] == mine:
        minecounter += 1
    if board[row][column+1] == mine:
        minecounter += 1
    if board[row+1][column-1] == mine:
        minecounter += 1
    if board[row+1][column+1] == mine:
        minecounter += 1
    if board[row-1][column-1] == mine:
        minecounter += 1
    if board[row-1][column+1] == mine:
        minecounter += 1
    return (minecounter)


def clueBoard(boardList):
    row = 1
    print (len(boardList))
    while row < (len(boardList)- 1 ) :
        col = 1
        mineClue = 0
        while col < (len(boardList[row])) -1 :
            if boardList[row][col] != boardMine and boardList[row][col] != border:
                mineClue = neighborNum(boardList, row, col)
                if mineClue > 0:
                    boardList[row][col] = mineClue
            col += 1
        row += 1
    return boardList

def flagMove(gameBoard, row, column, neighbors):
    if gameBoard[row][column] == "f":
         gameBoard[row][column] = "."
         print("Flag removed from", row,",", column)
    elif gameBoard[row][column] in neighbors: 
         print("This tile can not be flagged")
    else:
        gameBoard[row][column] = "f"
    return gameBoard

def revealMove(board,gameBoard, row, column, gameLost, neighbors):
    if board[row][column] == " ":
        numClue = neighborNum(board, row, column)
        if numClue > 0:
            gameBoard[row][column] = numClue
        if numClue == 0:
            gameBoard[row][column] = " "
    elif  board[row][column] == "f":
        print("Field 1, 1 must be unflagged before it can be revealed")
    elif board[row][column] == boardMine:
        gamesLost = True
    elif gameBoard[row][column] in neighbors:
        print()
    return gameBoard

def boardToList(board):
    newBoard = []
    row = 0
    while len(newBoard) < len(board):
        boardRow = []
        col = 0
        while len(boardRow) < len(board[row]):
            boardRow.append(board[row][col])
            col += 1
        row +=1    
        newBoard.append(boardRow)
    return newBoard


def playMove(board, boardList, gameBoard, neighbors):
    selections = getchoice(board)
    row = selections[0]
    column = selections[1]
    move = selections[2]
    if move == "f":
        playerBoard = flagMove(playerBoard, row, column, neighbors)
        prettyPrintBoard(playerBoard)
        numMines(board, playerBoard)
    if move == "r":
        playerBoard = revealMove(board, playerBoard, row, column, gameLost, neighbors)
        prettyPrintBoard(playerBoard)
        numMines(board, playerBoard)
    boardList = boardToList(board)
    newBoardList = clueBoard(boardList)

def island(boardList, gameBoard, row, col):
    borderClues = ["1","2","3","4","5","6","7","8","#"]
    if boardList[row][col] in borderClues:
        gameBoard[row][col] = boardList[row][col]
        return gameBoard
    else:
        gameBoard[row][col] = " "
        if row > 0:
            island(gameBoard, row - 1, col)
        if row < len(board[row]) - 1:
            island(gameBoard, row + 1, col)
        if col > 0:
            island(gameBoard, row, col - 1)
        if col < len(board) - 1:
            island(gameBoard, row, col + 1)

def winCheck(boardList, gameBoard,gameWon, minesLeft):
    row = 0
    while row < len(gameBoard):
        col = 0
        while col < len( gameBoard[row] ):
            if gameBoard[row][col] == "f" and boardList[row][col] == boardMine:
                wincheck += 1
            col += 1
        row += 1
    if winCheck == minesLeft:
        gameWon = True
            
def main():
    gameWon = False
    neighbors = ["1","2","3","4","5","6","7","8"," "]
    move = []
    boardList = []
    gameLost = False
    print("This program allows you to play Minesweeper. \n\tThe object of the game is to flag every mine,\n\tusing clues about the number of neighboring \n\tmines in each field.  To win the game, flag \n\tall of the mines (and don't incorrectly flag \n\tany non-mine fields).  Good luck!")
    boardNum = input("Enter the file to load the board from: ")
    gameBoard = open(boardNum)
    board = gameBoard.readlines()
    gameBoard.close
    playerBoard = createBoard(board)
    prettyPrintBoard(playerBoard)
    minesLeft = numMines(board, playerBoard)
    while gameLost == False and gameWon == False: 
        selections = getchoice(board)
        row = selections[0]
        column = selections[1]
        move = selections[2]
        if move == "f":
            playerBoard = flagMove(playerBoard, row, column, neighbors)
            prettyPrintBoard(playerBoard)
            numMines(board, playerBoard)
        if move == "r":
            playerBoard = revealMove(board, playerBoard, row, column, gameLost, neighbors)
            prettyPrintBoard(playerBoard)
            numMines(board, playerBoard)
        boardList = boardToList(board)
        newBoardList = clueBoard(boardList)
        winCheck(newBoardList, playerBoard,gameWon, minesLeft)
    if gameWon == True:
        print("You won! Congratulations, and good game!")
    if gameLost == True:
        print("You detonated a mine!  Game Over!")
main()

