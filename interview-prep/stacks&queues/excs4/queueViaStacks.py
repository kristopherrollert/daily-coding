# Queue via Stacks: Implement a MyQueue class which implements a queue using
# two stacks

# oh dang okay.

# niave approach: add: appends to top of one list, remove: shifts all elements
# over to other stack and takes the top off. Only shift when required

from stack import *

class QueueViaStacks:
    def __init__(self):
        self.removeStack = Stack()
        self.addStack = Stack()


    def add(self, val):
        while (not self.removeStack.isEmpty()):
            self.addStack.push(self.removeStack.pop())
        self.addStack.push(val)

    def remove(self):
        while (not self.addStack.isEmpty()):
            self.removeStack.push(self.addStack.pop())
        return self.removeStack.pop()


if __name__ == '__main__':
    q = QueueViaStacks()
    q.add(1)
    q.add(2)
    q.add(3)
    print(q.remove())
    q.add(4)
    print(q.remove())
    print(q.remove())
