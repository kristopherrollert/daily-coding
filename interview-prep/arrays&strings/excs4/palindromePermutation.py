# Palindrome Premutation: Given a string, write a function to check if its a
# permutation of a palidrome.

# ex: "tact coa" => true because "taco cat" and "atco cta"

import sys

# thoughts:
# so spaces actually don't really matter. ignore them
# traverse. Tally all letters. If len of string is even, then there must be an even amoutn of each
# if odd, there can be ONE not even amount. (keep track of this with boolean? => nah can't)
# bit vectors feel like they could work for this.
ASCII_OFFSET = 97

# Attempt 1: Got it!!!! This made me really understand bitwise vectors :)
def palindromePermutation1(str):
    strLen = 0
    check = 0 # bit vector to check that all are even
    oddNum = 0 # keeps track of how many are odd
    for c in str:
        if c != ' ':
            strLen += 1
            c_val = ord(c.lower()) - ASCII_OFFSET

            # if check_val is 0, then it is now odd, if it is 1, it is now even
            check_val = (check >> c_val) & 1
            oddNum += -1 if check_val else 1
            check ^= 1 << c_val # flips bit

    return ((strLen % 2) == 0 and oddNum == 0) or ((strLen % 2) == 1 and oddNum == 1)

if __name__ == '__main__':

    if len(sys.argv) != 1:
        print("palindromePermutation: %s" % (palindromePermutation1("".join(sys.argv[1:]))))
    else:
        print("palindromePermutation must be given exactly one command line argument")



# if words > 1, then grab each word on either side. Then check if the shorter one
# could fit into the other one. if not, done. If yes, then save the extra characters
# in OFFSET. then rerun program with the next words.


# func(startWord, endWord, strOffest, offsetSide)
# check if the letters in offset are in startWord/endWord (depending on offsetSide)
# if they aren't => return false
# if they are => remove those from that
