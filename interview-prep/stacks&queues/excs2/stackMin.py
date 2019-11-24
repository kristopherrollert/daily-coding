# Stack Min: How would you design a stack in which, in addition to push and pop
# has a function min which returns the minimum element? Push, pop, and min
# should all operate in O(1) time.

from stack import *

class MinStack:
    def __init__(self):
        self.mins = Stack()
        self.stack = Stack()

    def push(val):
        if (self.mins.isEmpty() or val <= self.mins.peek()):
            self.mins.push(val)
        self.stack.push(val)

    def pop():
        top = self.stack.pop()
        if (top == self.mins.peek()):
            self.mins.pop()
        return top

    def min(self):
        return self.min.peek()
