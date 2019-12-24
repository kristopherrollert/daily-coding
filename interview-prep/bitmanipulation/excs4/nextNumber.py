# Next Number: Given a positive integer, print the next smallest and the next largest number
# that have the same number of 1 bits in their binary representation.

# bigger, traverse => right to left to find first 1, make it 0, then continue
# traversing until you find a 0 bit. Then replace that with a 1.

# for smaller, traverse => left to right, find the first 0, make it a 1, and
# then traverse until you find a 0.

# does there exist an integer x s.t. 2^x -1 = num


# 0101010101
# 0101010110
# 0101011111
# right most 0, and then the next 1
# traverse right to left till you find a 0
# next biggest = making the smallest 0 into a 1 if there exists a 1 to the right
# of it to bump up

import math

def nextNumber(num):
    print("NUMBER: " + "{0:b}".format(num))
    if (num == 0):
        return "ERROR"

    place = 0
    found = False
    trav = 1
    bigger = None
    while (True):
        if (num & (1 << trav) != 0):
            found = True
            place = trav
        elif found:
            bigger = (num & ~(1 << place)) | (1 << trav)
            break
        trav += 1

    print("BIGGER: " + "{0:b}".format(bigger))

    if (math.log(num + 1, 2).is_integer()):
        return "ERROR"

    place = 0
    found = False
    trav = 1
    smaller = None
    while (True):
        if (num & (1 << trav) == 0):
            found = True
            place = trav
        elif found:
            smaller = (num & ~(1 << trav)) | (1 << place)
            break
        trav += 1

    print("SMALLER: " + "{0:b}".format(smaller))


nextNumber(27)
