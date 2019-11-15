

# go through the array, matching characters. Once you get to one that isn't
# matching, then you got your problem.

# have different indexs for each one? that way we can offset?
# break up into different functions for readability

# removeable cases:
# if string is more than 1 size larger => NO
# if string is 1 size larger: must, remove
# if string is 1 size smaller: must add
# if string is the same size: must swtich (or do nothing)

# switch:
# loop through, if a charcter is different, that's fine. Set didEdit = True
# if you get to another incorrect character, return false. Otherwise return tru

# add:
# loop through, until characters are different, then skip this letter and set didEdit = false
# if you get to another incorrect character, return false. Otherwise return tru

# remove:

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
