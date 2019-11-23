# Palindrome: Implement a function to check if a linked list is a palindrome.
import sys
import math
from linkedlist import *

# I could implement Attempt 1 with a stack. Then it would only require 1
# traversal

# Attempt 1: kinda stole this from a hint. It has O(n) time and O(n) space
def palindrome1(ll):
    if (ll.head is None or ll.head.next is None):
        return True

    rev_ll = LinkedList()
    second = ll.head
    back_curr = Node(second.val)
    first = ll.head.next
    while (first is not None):
        n = Node(first.val)
        n.next = back_curr
        back_curr = n
        second = first
        first = first.next

    rev_ll.head = back_curr

    curr1 = rev_ll.head
    curr2 = ll.head
    while (curr1 is not None):
        if (curr1.val != curr2.val):
            return False
        curr1 = curr1.next
        curr2 = curr2.next

    return True

# Attempt 2: I want to assume that I cannot use more than O(1) space, but not
# care as much about time. This one is going to be really slow but like that is
# the life.
def palindrome2(ll):
    # part one: get length and middle node
    k = 0
    middleNode = ll.head
    lengthNode = ll.head
    while (lengthNode is not None):
        k += 1
        lengthNode = lengthNode.next
        if (lengthNode is None): break
        k += 1
        lengthNode = lengthNode.next
        middleNode = middleNode.next

    if (k % 2 == 1):
        middleNode = middleNode.next


    curr = ll.head
    for i in range(math.floor(k/2) - 1, -1, -1):
        trav = middleNode
        for j in range(0, i):
            trav = trav.next
        if (curr.val != trav.val):
            return False
        curr = curr.next

    return True


if __name__ == '__main__':
    if len(sys.argv) == 2:
        ll = LinkedList()
        for c in sys.argv[1]:
            n = Node(c)
            if ll.head is None:
                ll.head = n
                curr = n
            else:
                curr.next = n
                curr = curr.next

        fill = "" if palindrome2(ll) else " not"
        print("%s is%s a palindrome\n" % (sys.argv[1], fill))
    else:
        print("palindrome must be given exactly one command line arguments")
