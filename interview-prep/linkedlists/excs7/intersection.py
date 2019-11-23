# Intersection: Given two singly linked lists, determine if the two lists
# intersect. Return the intersecting node.

import sys
import random
from linkedlist import *

# Attempt 1: Using a hash table
def intersection1(ll1, ll2):
    d = {}
    curr1 = ll1.head
    curr2 = ll2.head
    while (curr1 is not None or curr2 is not None):
        if (curr1 is not None):
            if (curr1 in d):
                return [True, curr1]
            d[curr1] = True
            curr1 = curr1.next
        if (curr2 is not None):
            if (curr2 in d):
                return [True, curr2]
            d[curr2] = True
            curr2 = curr2.next
    return [False, None]


# Solution: of course way smarter dang. We know that two intersecting linked
# lists have the same last node. Then we've gotta calculate the linked lists
# intersection. Once we know the length of both lists, we can cut off the
# 'extra' of the longer list. The 'extra' is equal to the bigger list's length
# minus the small lists length. We start 'extra' .next's into the bigger list
# and compare until we find the same node. Brilliant.
def intesection2(ll1, ll2):
    # first: check if the last element is equal and keep track of length
    curr1 = ll1.head
    ll1_len = 0
    while (curr1 is not None):
        ll1_len += 1
        curr1 = curr1.next

    curr2 = ll2.head
    ll2_len = 0
    while (curr2 is not None):
        ll2_len += 1
        curr2 = curr2.next

    if (curr1 != curr2):
        return [False, None]

    diff = abs(ll1_len - ll2_len)
    [longerll, shorterll] = [ll1, ll2] if ll1_len > ll2_len else [ll2, ll1]
    curr1 = longerll.head
    curr2 = shorterll.head
    for i in range(0, diff):
        curr1 = curr1.next

    while (curr1 != curr2):
        curr1 = curr1.next
        curr2 = curr2.next

    return [True, curr1]

if __name__ == '__main__':
    if len(sys.argv) == 4:
        len1 = int(sys.argv[1])
        len2 = int(sys.argv[2])
        intersect = sys.argv[3] == "True"

        ll1 = LinkedList()
        curr1 = Node(random.randint(1,5))
        ll1.head = curr1
        for i in range(1, len1 - 1):
            curr1.next = Node(random.randint(0,9))
            curr1 = curr1.next

        ll2 = LinkedList()
        curr2 = Node(random.randint(0,9))
        ll2.head = curr2
        for i in range(1, len2 - 1):
            curr2.next = Node(random.randint(0,9))
            curr2 = curr2.next

        if (intersect):
            doubleNode = Node(random.randint(0,9))
            curr1.next = doubleNode
            curr2.next = doubleNode
            for i in range(1, random.randint(1,5)):
                doubleNode.next = Node(random.randint(0,9))
                doubleNode = doubleNode.next

        print("List 1:\n", ll1)
        print("List 2:\n", ll2)
        [ok, n] =  intersection1(ll1, ll2)
        if ok:
            print("insersection:", ok, n.val)
        else:
            print("insersection:", ok)
    else:
        print("removeDuplicates must be given exactly two command line arguments. \
        first the length of the first list, second the length of the second, third \
        if they intersect [True, False]")
