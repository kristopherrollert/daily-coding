class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        n = Node(val)
        n.next = self.top
        self.top = n

    def pop(self):
        if (self.top is None):
            raise Exception("Stack is Empty")
        item = self.top
        self.top = self.top.next
        return item.val

    def peek(self):
        if (self.top is None):
            raise Exception("Stack is Empty")
        return self.top.val

    def isEmpty(self):
        return self.top is None

    def __str__(self):
        n = self.top
        strFmt = ""
        while (n is not None):
            strFmt += ("| " + str(n.val) + " | -> ")
            n = n.next
        strFmt += 'None'
        return strFmt
