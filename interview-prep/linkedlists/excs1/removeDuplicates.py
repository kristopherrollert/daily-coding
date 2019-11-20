# Remove Duplicates: Write code to remove duplicates from an unsorted linked
# list. Followup: how would you solve this problem if a temporary buffer is
# no allowed?

from linkedlist import *
import sys
import random

# I am unsure when it says duplicates does it mean back to back or just two of
# the same? I am going to solve both.

# Attempt 1: with buffer (hashmap) looking for any duplicates
def removeDuplicates1(ll):
    if (ll.head is None or ll.head.next is None):
        return

    check = {ll.head.val: True}
    prev = ll.head
    curr = ll.head.next
    while (curr is not None):
        if curr.val in check:
            prev.next = curr.next
            curr = curr.next
        else:
            check[curr.val] = True
            prev = curr
            curr = prev.next

# Attempt 2: assuming multiple in a row
def removeDuplicates2(ll):
    if (ll.head is None or ll.head.next is None):
        return

    start = ll.head
    curr = ll.head.next
    cutRequired = False
    while (curr is not None):
        if start.val == curr.val:
            cutRequired = True
            curr = curr.next
        else:
            if cutRequired:
                start.next = curr
            start = curr
            curr = curr.next

# Attempt 3: duplicates throughout without buffer

if __name__ == '__main__':
    if len(sys.argv) == 2:


        ll = LinkedList()
        curr = Node(random.randint(1,5))
        ll.head = curr
        for i in range(0, int(sys.argv[1]) - 1):
            curr.next = Node(random.randint(1,5))
            curr = curr.next

        print("Before duplicates are removed:\n", ll)
        removeDuplicates2(ll)
        print("After duplicates are removed:\n", ll)
    else:
        print("removeDuplicates must be given exactly one command line argument.")
