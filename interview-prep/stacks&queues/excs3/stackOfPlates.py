# A STACK OF STACKS???
# this would require a lot of peeking. which kinda defeats the purpose of a
# stack? well maybe not its still O(n) time, and when you run out you can
# just pop it off or if you need another one just push it on.

# How do we solve popAtIndex(index)? we would have to traverse the stack
# To speed up we could do a hash table that links indexes to stacks?
# Then you don't have to pop stack unneccesarily. But that seems like
# more space?

from stack import *

class StackOfStacks:
    def __init__(self, maxInStack):
        self.maxInStack = maxInStack
        self.stacksStack = Stack()
        self.d = {}
        s = Stack()
        self.d[0] = s
        self.stacksStack.push(s)
        self.currentNumber = 1
        self.stacks = 0

    def push(val):
        if (currentNumber == maxInStack):
            s = Stack()
            self.stacks += 1
            self.d[self.stacks] = s
            self.stacksStack.push(s)
            self.currentNumber = 0

        self.stacksStack.peek().push(val)
        self.currentNumber += 1

    def pop():
        self.currentNumber -= 1
        temp = self.stacksStack.peek().pop()

        if (self.stacksStack.peek().isEmpty() and self.stacks != 0):
            self.stacksStack.pop()
            self.currentNumber = maxInStack
            del self.d[self.stacks]
            self.stacks -= 1

        return temp

    def popAtIndex(i):
        return d[i].pop()
