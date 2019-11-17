# String Compression: Implement a method to perform basic string compression
# using the counts of repeated characterss.
# EX: aabcccccaaa => a2b1c5a3.
# if you compressed string would not be smaller than the original string, your
# method should return the original string. You can assume that the string
# has only uppercase and lowercase letters

import sys

# idea: traverse the array keeping track of the last character, when a new
# character is reached, create the new string.

def stringCompression1(str):
    new_str = []
    new_len = 0
    old_len = len(str)
    old_char = str[1]
    count = 1
    for c in str[1:]:
        if c != old_char:
            new_str.append("%s%d" %(old_char, count))
            new_len += 2
            if new_len > old_len:
                return str
            count = 1
            old_char = c
        else:
            count += 1
    new_str.append("%s%d" %(old_char, count))
    return str if new_len > old_len else "".join(new_str)


if __name__ == '__main__':

    if len(sys.argv) == 2:
        print("stringCompression: %s" % (stringCompression1(sys.argv[1])))
    else:
        print("stringCompression must be given exactly one command line argument")
