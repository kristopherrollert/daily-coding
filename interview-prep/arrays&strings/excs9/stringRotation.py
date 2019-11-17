# String Rotation: Assume you have a method isSubstring which checks if one word
# is a substring of another. Given two strings s1 and s2, write code to check if
# s2 is a rotation of s1 using only one call to isSubstring

import sys

def isSubstring(s1, s2):
    return s1 in s2

# Attempt 1: I was pretty proud of this, but it isn't optimal
def stringRotation1(s1, s2):
    # traverse s2 looking for the first characters of s1 such that it end
    if len(s1) != len(s2):
        return False

    s1_index = 0
    start = 0
    for s2_index in range(len(s2)):
        if (s1[s1_index] == s2[s2_index]):
            s1_index += 1
            if start == 0:
                start = s2_index
        elif s1[0] == s2[s2_index]:
            s1_index = 1
            start = s2_index
        else:
            s1_index = 0
            start = 0

    if s1_index == 0:
        return False

    return isSubstring(s2[:start], s1)

# Solution:
def stringRotation2(s1, s2):
    if (len(s1) == len(s2) and len(s1) > 0):
        double_s1 = "".join(list(s1) + list(s2))
        return isSubstring(s2, double_s1)
    return false


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print("stringCompression: %s" % (stringRotation1(sys.argv[1], sys.argv[2])))
    else:
        print("stringCompression must be given exactly two command line arguments")
