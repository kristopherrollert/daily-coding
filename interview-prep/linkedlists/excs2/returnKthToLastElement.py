# Return kth to Last: Implement an algorithm to find the kth to last element
# of a singly linked list
import sys
import random
from linkedlist import *

def kthToLastElement(ll, k):
    node = ll.head
    offset = ll.head
    for i in range(k):
        if (offset is None):
            return -1
        offset = offset.next

    while offset is not None:
        node = node.next
        offset = offset.next

    return node.val

if __name__ == '__main__':
    if len(sys.argv) == 3:

        ll = LinkedList()
        curr = Node(random.randint(1,5))
        ll.head = curr
        for i in range(0, int(sys.argv[1]) - 1):
            curr.next = Node(random.randint(1,5))
            curr = curr.next

        print("List:\n", ll)
        print("Kth to last element:\n", kthToLastElement(ll, int(sys.argv[2])))
    else:
        print("removeDuplicates must be given exactly two command line arguments. \
            First the length of the randonly valued list, then the k value")
