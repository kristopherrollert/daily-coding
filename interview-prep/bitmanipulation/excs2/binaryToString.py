# Binary to String: Given a real number between 0 and 1 that is passed as a
# double, print the binary representation. If the numner cannot be represented
# with at most 32 characters, print "ERROR"

def binaryToString(num):
    m = .5
    l = "."
    while (num != 0):
        if (num >= m):
            num -= m
            l += "1"
        else:
            l += "0"
        m *= .5
        if (len(l) > 32):
            print("ERROR")
            return
    print(l)

binaryToString(.423532543)
