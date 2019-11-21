# Delete Middle Node: Implement an algorithm to delete a node in the middle
# (i.e. any node but the first and last node, not necessarily the exact middle)
# of a singly linked list, given only access to that node

import sys
import random
from linkedlist import *

# Attempt 1: this one seems really trivial and I am scared
def deleteMiddleNode(delNode, ll):
    prev = ll.head
    curr = ll.head.next
    while (curr is not None):
        if curr == delNode:
            prev.next = curr.next
            curr.next = None
            return
        prev = prev.next
        curr = curr.next


if __name__ == '__main__':
    if len(sys.argv) == 3:
        ll = LinkedList()
        delNum = int(sys.argv[2]) - 2
        delNode = 5
        curr = Node(random.randint(1,5))
        ll.head = curr
        for i in range(0, int(sys.argv[1]) - 1):
            curr.next = Node(random.randint(1,5))
            curr = curr.next
            if i == delNum:
                delNode = curr

        print("List:\n", ll)
        deleteMiddleNode(delNode, ll)
        print("New list after deletion:\n", ll)
    else:
        print("removeDuplicates must be given exactly two command line arguments. \
            First the length of the randomly valued list, then the index to delete")
