# One Away: there are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character. Given two
# strings, write a function to check if they are one edit (or zero edits) away

import sys

# remove and add are the same, depending on which string is first
def oneAway1(str1, str2):
    # order large one first for ease
    [str1, str2] = [str1, str2] if len(str1) > len(str2) else [str2, str1]
    sizeDiff = len(str1) - len(str2)
    if sizeDiff == 1:
        return removeOneAway(str1, str2)
    elif sizeDiff == 0:
        return switchOneAway(str1, str2)
    return False


def removeOneAway(str1, str2):
    offset = 0
    str2 += " " # to prevent out of bounds error
    # traversing through the length of the larger string.
    for i in range(len(str1)):
        if str1[i] != str2[i - offset]:
            if offset == 1:
                return False
            offset = 1
    return True


def switchOneAway(str1, str2):
    didEdit = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if didEdit:
                return False
            didEdit = True
    return True



if __name__ == '__main__':

    if len(sys.argv) == 3:
        print("oneAway: %s" % (oneAway1(sys.argv[1], sys.argv[2])))
    else:
        print("oneAway must be given exactly two command line argument")
