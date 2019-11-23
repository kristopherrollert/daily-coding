class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        n = self.head
        strFmt = ""
        while (n is not None):
            strFmt += ("| " + str(n.val) + " | -> ")
            n = n.next
        strFmt += 'None'
        return strFmt
