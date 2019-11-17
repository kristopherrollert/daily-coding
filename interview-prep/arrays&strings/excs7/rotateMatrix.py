# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel
# in the image is 4 bytes, write a method to rotate the image by 90 degrees.
# Can you do it in place?

import sys
import math
import random

# Attempt 1: My god I got it! It is in-place!
def rotateMatrix1(M):

    N = len(M)
    O = math.floor(N / 2)

    for ii in range(O):
        for jj in range(ii, (N - 1) - ii):
            i = M[ii][jj] # top
            j = M[jj][(N - 1) - ii] # right
            k = M[(N - 1) - ii][(N - 1) - jj] # bottom
            l = M[(N - 1) - jj][ii] # left

            M[ii][jj] = l # set top to left
            M[jj][(N - 1) - ii]  = i # set left to top
            M[(N - 1) - ii][(N - 1) - jj] = j # set botton to right
            M[(N - 1) - jj][ii] = k # set left to bottom

    return M

def generateRandomMatrix(N):
    return [[random.randint(0, 99) for i in range(N)] for j in range(N)]

def printMatrix(N, ):
    matrixLen = len(N)
    for i in range(matrixLen):
        for j in range(matrixLen):
            print(" %2d" %(N[i][j]), end=' ')
        print()


if __name__ == '__main__':

    if len(sys.argv) == 2:
        NLen = int(sys.argv[1])
        N = generateRandomMatrix(NLen)
        print("Randomly generated matrix of size %d by %d:" % (NLen, NLen))
        printMatrix(N)
        print()
        N = rotateMatrix1(N)
        print("Matrix rotated clockwise:")
        printMatrix(N)
    else:
        print("rotateMatrix must be given exactly one command line argument")
