# Minimal Tree: given a shorted (increasing order) array with unqiue integer
# elements, write an alogirthm to create a binary search tree with minimal
# height

# if the array is x long, then ceil(log(x, 2)) gives the min level
# the hard part is going to be doing it recursively i guess

# get the middle element? move left and right

# its like merge sort kinda
# go recursively down the middle
# get middle element, recruvely run left side of alg on left side of array
# and set that to left ndoe
# do the same for right
# base case is when you have one element, return that element

import math

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def minimalTree(arr, start, end):
    if (end < start):
        return None
    mid = math.floor((end + start) / 2)
    me = Node(arr[mid])

    me.left = minimalTree(arr, start, mid - 1)
    me.right = minimalTree(arr, mid + 1, end)
    return me

def recursivePrint(node, i):
    if (node is not None):
        recursivePrint(node.left, i+ 1)
        print(node.val, i)
        recursivePrint(node.right, i + 1)



if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    node = minimalTree(arr, 0, len(arr) - 1)
    recursivePrint(node, 0)
