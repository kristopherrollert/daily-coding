# Loop Detection: Given a circular linked list, implement an algorithm that
# returns the node at the beginning of the loop
import sys
import random
from linkedlist import *

def loopDetetction1(ll):
    curr = ll.head
    d = {}
    while (True):
        if (curr is None):
            return [False, None]
        d[curr] = True
        if (curr.next in d):
            return [True, curr.next]
        curr = curr.next


# Solution: fucking wild
def loopDetetction2(ll):
    fast = ll.head
    slow = ll.head

    while (True):
        if (fast.next is None or fast.next.next is None):
            return [False, None]
        slow = slow.next
        fast = fast.next.next
        if (fast == slow): break

    slow = ll.head
    while (True):
        if (fast == slow):
            return [True, fast]
        fast = fast.next
        slow = slow.next


if __name__ == '__main__':
    length = random.randint(1,10)
    loopTo = random.randint(1,length)
    loopToNode = None

    ll = LinkedList()
    curr = None
    for i in range(1, length + 1):
        n = Node(i)
        print("|%d|" % (n.val), end=' -> ')
        if (i == loopTo):
            loopToNode = n

        if (ll.head is None):
            ll.head = n
            curr = n
        else:
            curr.next = n
            curr = curr.next

    print("|%d|" %(loopToNode.val))
    curr.next = loopToNode
    [ok, node] = loopDetetction2(ll)
    if (ok):
        print("loop originates at:", node.val)
    else:
        print("no loop")
