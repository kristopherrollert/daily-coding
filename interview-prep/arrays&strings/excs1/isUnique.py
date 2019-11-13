# Is Unique: Implement an alogrithm to determine if a string has all unique
# characters. What if you cannot use additional data stuctures?

import sys

# Attempt 1: Using build in hash table
# O(N)
def isUnique1(str):
    str = str.lower()
    d = {}
    for c in str:
        if c in d: return False
        d[c] = True
    return True

# Attempt 2: Not using additional data structures. I sort the array and check
# for duplicates
# O(N * log(N) + N) = O(N * Log(N))
def isUnique2(str):
    str = str.lower()
    strSorted = sorted(str)
    for i in range(len(str) - 1):
        if strSorted[i] == strSorted[i + 1]:
            return False
    return True

# Solution 2: Use a bit vector to reduce space usage by a factor of 8
def isUnique3(str):
    str = str.lower()
    check = 0
    for c in str:
        n = ord(c) - 97 # SCII value for a
        if (check >> n) & 1: return False
        check |= 1<<n
    return True


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            print("%s: %r" % (arg, isUnique3(arg)))
    else:
        print("isUnique must be given one command line argument")
