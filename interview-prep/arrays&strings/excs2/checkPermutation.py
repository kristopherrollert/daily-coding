# Check Permutation: Given two strings, write a method to decide if one is a
# permutation of the other

import sys

# Attempt 1: have an alphabet sized array that is incremented in each character
# location for str1 and decremented in each character location for str2. Once
# complete loop through array to ensure that the array is equal to 0
def checkPermutation1(str1, str2):
    if len(str1) != len(str2):
        return False

    asciiOffset = 97
    check = [0 for i in range(26)]
    str1, str2 = str1.lower(), str2.lower()

    for index in range(len(str1)):
        check[ord(str1[index]) - asciiOffset] += 1
        check[ord(str2[index]) - asciiOffset] -= 1

    for val in check:
        if val != 0:
            return False
    return True

# Solution: same as attempt but it includes small optmization where you put
# str1 into the array and then st2, but you can end early if it ever goes
# negitive
def checkPermutation2(str1, str2):
    if len(str1) != len(str2):
        return False

    asciiOffset = 97
    check = [0 for i in range(26)]
    str1, str2 = str1.lower(), str2.lower()

    for index in range(len(str1)):
        check[ord(str1[index]) - asciiOffset] += 1

    for index in range(len(str2)):
        loc = ord(str2[index]) - asciiOffset
        newVal = check[loc] - 1

        if newVal < 0: return False
        else: check[loc] = newVal

    for val in check:
        if val != 0:
            return False
    return True

if __name__ == '__main__':
    if len(sys.argv) == 3:
        notString = "" if checkPermutation2(sys.argv[1], sys.argv[2]) else "not "
        print("The strings are %spermutations" % (notString))
    else:
        print("checkPermutation must be given exactly two command line arguments")
