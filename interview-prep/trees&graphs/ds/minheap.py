# Minheap data structure review

import math

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class MinHeap:
    def __init__(self):
        self.root = None
        self.nodes = 0

    def insertLast(self, parentNode, nodeToInsert, level):
        # recursively search through level. This is done by recursively
        # searching the level above where it is supposed to be going from left
        # to right until you find an open spot
        # how do we find the correct level above the insert? if you are inserting
        # the ith node, you need to find the largest x s.t. 2^x - 1 < i
        # math.floor(log(i + 1, 2)) = x

        if (level == 1): # you are at the correct level for a parent
            if (parentNode.left is not None):
                parentNode.left = nodeToInsert
                return True
            elif (parentNode.right is not None):
                parentNode.right = nodeToInsert
                return True
            return False

        ok = insertLast(self, parentNode.left, nodeToInsert, level - 1)
        if (ok): return True
        ok = insertLast(self, parentNode.right, nodeToInsert, level - 1)
        return ok

    def insert(self, val):
        self.nodes += 1
        level = math.floor(math.log(self.nodes, 2))
        if (self.root is None):
            self.root = Node(val)
        else:
            s = self.insertLast(self.root, Node(val), level)
        # need to keep track of where to insert element?
        # what level?
        #  2^level = max_nodes
        # keep track of level instead?
        # we could just traverse till you find the last

    def traversePrint(self, node):
        if (node is None):
            print("| |", end='')
        self.traversePrint(node.left)
        self.traversePrint(node.right)
        print("|%d| " % node.val, end ='')

    def print()

if __name__ == '__main__':
    s = MinHeap()
    s.insert(5)
    s.insert(10)
    s.insert(11)

    # def getmin(self):
