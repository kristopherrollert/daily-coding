# Partition: Write code to partition a linked list around a value x, such that
# all nodes greater than or equal to x. If x is contained within the list, the
# values of x only need to be after the elements less than x. The partition
# element x can appear anywhere in the "right partition"; it does not need to
# appear between the left and right partitions

import sys
import random
from linkedlist import *

# Attempt 1:
# loop through the list. for each node, append it to left or right linked list
# at the end append
def partition1(ll, x):
    leftNode = None
    leftHead = None
    rightNode = None
    rightHead = None
    curr = ll.head

    while (curr is not None):
        if curr.val < x: # left
            if leftNode is not None:
                leftNode.next = curr
            else:
                leftHead = curr
            leftNode = curr
        else: # right
            if rightNode is not None:
                rightNode.next = curr
            else:
                rightHead = curr
            rightNode = curr
        curr = curr.next


    if leftNode is not None:
        leftNode.next = rightHead

    if rightNode is not None:
        rightNode.next = None

    ll.head = leftHead


if __name__ == '__main__':
    if len(sys.argv) == 3:
        ll = LinkedList()
        xVal = int(sys.argv[2])
        curr = Node(random.randint(1,9))
        ll.head = curr
        for i in range(0, int(sys.argv[1]) - 1):
            curr.next = Node(random.randint(1,5))
            curr = curr.next

        print("List:\n", ll)
        partition1(ll, xVal)
        print("New list after partition:\n", ll)
    else:
        print("removeDuplicates must be given exactly two command line arguments. \
            First the length of the randomly valued list, the value to partition \
            around")
