# Flip Bit to Win: You have an integer and you can flip exactly one bit from a
# 0 to a 1. Write code to find the length of the longest sequence of 1s
# you could create

def flipBitToWin(num):
    first = 0
    second = 0
    most = 0
    for curr in "{0:b}".format(num):
        if (curr == "0"):
            first = second
            second = 0
        else:
            second += 1

        if (first + second + 1 > most):
            most = first + second + 1
    return most

print(flipBitToWin(256))
