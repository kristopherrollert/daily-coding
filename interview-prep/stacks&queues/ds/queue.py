class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, val):
        n = Node(val)
        if (self.last is not None):
            self.last.next = n
        self.last = n
        if (self.first is None):
            self.first = n

    def remove(self):
        if (self.first is None):
            raise Exception("Queue is Empty")
        n = self.first
        self.first = self.first.next
        if (self.first is None):
            last = None
        return n.val

    def peek(self):
        if (self.first is None):
            raise Exception("Stack is Empty")
        return self.first.val

    def isEmpty(self):
        return self.first is None

    def __str__(self):
        n = self.first
        strFmt = ""
        while (n is not None):
            strFmt += ("| " + str(n.val) + " | -> ")
            n = n.next
        strFmt += 'None'
        return strFmt
