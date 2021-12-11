# Solving Knights Tour with Warndorff's Algorithm

# define the chess board globally/ we're going to solve this for 8
# we're going to have a 2-demensional list with a total of 64 cells (8*8)
board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

# define the print board function


def printBoard():
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=" ")
        print("\n")

# define solution for all of the list of possibilites or chances
# There are 8 possibilities, but we have to make sure we don't move outside of the board
# We're going to define 2 tuples that cross the board horizontically & vertically

# These 2 tuples will define how much the positon has to change to move to its new
        # position. From these positions you can move to 8 other positions


def getChances(x, y):
    positionX = (2, 1, 2, 1, -2, -1, -2, -1)
    positionY = (1, 2, -1, -2, 1, 2, -1, -2)
    chances = []
    for i in range(8):
        if x+positionX[i] >= 0 and x + positionX[i] <= 7 and y+positionY[i] >= 0 and y + positionY[i] <= 7 and board[x + positionX[i]][y + positionY[i]] == 0:
            chances.append([x + positionX[i], y + positionY[i]])
    return chances

# implement the Warndorff's algorithm -- we have to find which cell has minimum chances
# we will have to get the lengths of each cell and get the minimum one


def solution():

    # we are start our count at 2 & automatically the 1 board cell is filled with the 1 element
    #   since we want to start at the first element
    count = 2
    x = 0
    y = 0
    for i in range(63):
        position = getChances(x, y)
        minElement = position[0]
        # compare the minimum element to the other elements
        # we are checking for a smaller value
        for pos in position:
            if len(getChances(pos[0], pos[1])) <= len(getChances(minElement[0], minElement[1])):
                minElement = pos

        x = minElement[0]
        y = minElement[1]
        board[x][y] = count

        # this will fill the whole board for us
        count = count + 1


solution()
printBoard()  # The Knight will visit each cell on the board 1 to 64
