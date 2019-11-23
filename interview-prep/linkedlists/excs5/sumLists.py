import sys
import random
from linkedlist import *

# Attempt 1
def sumLists(numList1, numList2):
    sumList = LinkedList()
    sumCurr = None
    curr1 = numList1.head
    curr2 = numList2.head
    next = 0
    while (curr1 is not None or curr2 is not None):
        val1 = 0 if curr1 is None else curr1.val
        val2 = 0 if curr2 is None else curr2.val
        total = (val1 + val2 + next) % 10
        next = int((val1 + val2 + next) / 10)
        n = Node(total)
        if (sumCurr is None):
            sumList.head = n
            sumCurr = n
        else:
            sumCurr.next = n
            sumCurr = n

        if (curr1 is not None):
            curr1 = curr1.next
        if (curr2 is not None):
            curr2 = curr2.next

    if (next != 0):
        sumCurr.next = Node(next)

    return sumList


if __name__ == '__main__':
    if len(sys.argv) == 3:
        ll1 = LinkedList()
        curr = Node(random.randint(1,5))
        ll1.head = curr
        for i in range(0, int(sys.argv[1]) - 1):
            curr.next = Node(random.randint(0,9))
            curr = curr.next

        ll2 = LinkedList()
        curr = Node(random.randint(0,9))
        ll2.head = curr
        for i in range(0, int(sys.argv[2]) - 1):
            curr.next = Node(random.randint(0,9))
            curr = curr.next

        print("List1:\n", ll1)
        print("List2:\n", ll2)
        print("List Sum:\n", sumLists(ll1, ll2))
    else:
        print("removeDuplicates must be given exactly two command line arguments. \
            First the length of the randomly valued list, then the k value")
