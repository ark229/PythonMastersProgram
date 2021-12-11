# solve Knights Tour algorithm using the Backtracking algorithm to compare effiencieny
# Backtracking is a technique where the goal is to get all solutions to a problem using the brute force approach.
# It consists of building a set of all the solutions incrementally.

num = 8


def chances(x, y, chessboard):

    if(x >= 0 and y >= 0 and x < num and y < num and chessboard[x][y] == -1):
        return True
    return False


def printboard(chessboard):

    for i in range(num):
        for j in range(num):
            print(chessboard[i][j], end=" ")
        print()


def solution():

    chessboard = [[-1 for i in range(num)] for i in range(num)]

    posX = [2, 1, 2, 1, -2, -1, -2, -1]
    posY = [1, 2, -1, -2, 1, 2, -1, -2]

    chessboard[0][0] = 0

    position = 1

    if(not solveSolution(chessboard, 0, 0, posX, posY, position)):
        print("No Solution")
    else:
        printboard(chessboard)


def solveSolution(chessboard, currentX, currentY, posX, posY, position):

    if(position == num ** 2):
        return True

    for i in range(8):
        newposX = currentX + posX[i]
        newposY = currentY + posY[i]
        if(chances(newposX, newposY, chessboard)):
            chessboard[newposX][newposY] = position
            if(solveSolution(chessboard, newposX, newposY, posX, posY, position + 1)):
                return True

            chessboard[newposX][newposY] = -1
    return False


if __name__ == "__main__":
    solution()

# The Knight will visit each cell on the chessboard (0 to 63)
