# Route Between Nodes: Given a directed graph, design an algorithm to find out
# whether there is a route between two nodes.

from queue import *

class Node:
    def __init__(self, children):
        self.children = children
        self.visitedA = False
        self.visitedB = False


def routBetweenTwoNodes(nodeA, nodeB):
     # let use bidirecitonal search!
    queueA = Queue()
    queueA.add(nodeA)
    queueB = Queue()
    queueB.add(nodeB)

    # how do I keep track of visited nodes? in the datasructure
    while (not queueA.isEmpty() or not queueB.isEmpty())
        if (not queueA.isEmpty()):
            curr = queueA.remove()
            curr.visitedA = True
            for child in curr.children:
                if child.visitedB:
                    return True
                if not child.visitedA:
                    queueA.add(child)

        if (not queueB.isEmpty()):
            curr = queueB.remove()
            curr.visitedB = True
            for child in curr.children:
                if child.visitedA:
                    return True
                if not child.visitedB:
                    queueA.add(child)

    return False


if __name__ == "__main__":
    
