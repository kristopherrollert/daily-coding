# Zero Matrix: Write an alogirthm such that if an element in an MxN Matrix is 0,
# its entire row and column are set to zero

# NOTES:
# you don't want to redudandly set bits to zero!!
# you are going to have to traverse the whole array, that is unavoidable
# once you found a zero, you don't need to traverse the rest of the column/row

# we can do it in place

import sys
import random

# Attempt 1:
# when traversing spot, save the columns and rows that need to be wiped
# then wipe all rows that need to be wiped
# then traverse all rows that need to be wipe by columns that aren't already wiped
# and wipe them
#
# therefore the minimum amount of data we need it the rows to wipe [only], columns to wipe [only], and columns that aren't wiped
ZERO_ROW = -1
def zeroMatrix1(N):
    rows = [i for i in range(len(N))]
    cols = [j for j in range(len(N[0]))]
    rowsToClear = []

    for row in rows:
        for col in cols:
            if col != ZERO_ROW:
                if N[row][col] == 0:
                    cols[col] = ZERO_ROW
                    rowsToClear.append(row)

    for i in range(len(cols)):
        if cols[i] == ZERO_ROW:
            # clear whole column
            for row in rows:
                N[row][i] = 0
        else:
            # go through clear rows and clear them
            for row in rowsToClear:
                N[row][i] = 0



# similar to before except that we use O(N) space to store rows/columns where
# we can do it in the matrix (oh wow) by using the first column
def zeroMatrix2(N):
    # check if the first row has any zeros, if so, set boolean firstRowZero to true
    # check if the first col has any zeros, if so, set boolean firstColZero to true

    # then travers the rest of the matrix. If you find a zero at i,j, set
    # N[i][0] and N[0][j] to zero

    # traverse the first row and column again using it to check if the row
    # should be wiped
    firstRowZero = False
    firstColZero = False

    # check if the first col has any zeros
    for row in N:
        if row[0] == 0:
            firstColZero = True
            break

    # check if the first row has any zeros
    for col in N[0]:
        if col == 0:
            firstRowZero = True
            break

    # loop through rest of matrix checking for 0s and saving them in the
    # first row/col of the matrix
    for row in range(1, len(N)):
        for col in range(1, len(N[0])):
            if N[row][col] == 0:
                N[row][0] = 0
                N[0][col] = 0

    # for each 0 in the first col, set the items of that row to 0
    for row in range(len(N)):
        if N[row][0] == 0:
            for col in range(len(N[0])):
                N[row][col] = 0

    # for each 0 in the first column, set the items of that column to 0
    for col in range(len(N[0])):
        if N[0][col] == 0:
            for row in range(len(N)):
                N[row][col] = 0

    if firstColZero:
        for row in N:
            row[0] = 0

    if firstRowZero:
        N[0] = [0] * len(N[0])


def generateRandomMatrix(N, M):
    return [[random.randint(0, 9) for i in range(M)] for j in range(N)]

def printMatrix(N):
    for row in N:
        for item in row:
            print(" %2d" %(item), end=' ')
        print()


if __name__ == '__main__':

    if len(sys.argv) == 3:
        NLen = int(sys.argv[1])
        MLen = int(sys.argv[2])
        N = generateRandomMatrix(NLen, MLen)
        print("Randomly generated matrix of size %d by %d:" % (NLen, MLen))
        printMatrix(N)
        print()
        zeroMatrix2(N)
        print("Matrix zero'd:")
        printMatrix(N)
    else:
        print("zeroMatrix must be given exactly two command line arguments: \
        a row length and a column length")



# when traversing spot, save the columns and rows that need to be wiped
# then wipe all rows that need to be wiped
# then traverse all rows that need to be wipe by columns that aren't already wiped
# and wipe them
#
# therefore the minimum amount of data we need it the rows to wipe [only], columns to wipe [only], and columns that aren't wiped
