# Sort Stack: Write a program to sort a stack such that the smallest items are
# on the top. You can use an additional temporary stack, but you may not copy
# the elements into any other data structure. The stack support the following
# operations: push, pop, peek, and isEmpty

# This is another case of 'what is the question actually asking'? Do they want
# me to sort a queue or have a queue that is always sorted

# Brainstorming...
from stack import *

# Attempt 1: this feels slow af but the idea
def sortStack(s):
    if (s.isEmpty()): return

    temp = Stack()
    temp.push(s.pop())

    while(not s.isEmpty()):
        toSort = s.pop()
        if (toSort <= temp.peek()):
            temp.push(toSort)
        else:
            while(not temp.isEmpty() and temp.peek() < toSort):
                s.push(temp.pop())
            temp.push(toSort)
    return temp


if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.push(3)
    s.push(8)
    s.push(9)
    s.push(1)
    s.push(12)
    print(sortStack(s))
