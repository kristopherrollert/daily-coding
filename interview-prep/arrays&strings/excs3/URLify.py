# URLify: Write a method to replace all spaces in a string with '%20'. You may
# assume that the string has sufficient space at the end to hold the additional
# characters, and that you are given the true length of the string

import sys

# Attempt 1: (got it right!)
def URLify1(str_list, size):
    size -= 1
    revPoint = len(str_list) -1
    for i in range(size, -1, -1):
        c = str_list[i]
        if c == ' ':
            str_list[revPoint] = '0'
            revPoint -= 1
            str_list[revPoint] = '2'
            revPoint -= 1
            str_list[revPoint] = '%'
        else:
            str_list[revPoint] = str_list[i]
        revPoint -= 1
    return "".join(str_list)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print("URLified: %s" % (URLify1(list(sys.argv[1]), int(sys.argv[2]))))
    else:
        print("URLified must be given exactly two command line arguments: the \
        the first being a string enclosed in quotes, the second an integer")
