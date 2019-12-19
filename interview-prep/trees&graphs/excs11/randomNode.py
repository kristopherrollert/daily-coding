# Random Node: you are implementing a binary tree class from scratch which, in
# addition to insert, find, and delete, has a method getRandomNode() which
# returns a random node from the tree. All nodes should be equally likely
# to be chosen. Design and implement an algorithm for getRandomNode and explain
# how you would implement the rest of the methods

# So I wrote out my answer, but it is correct!
# just keep track of left nodes, randomly generate a number, and you can
# recursively subtract the amount of nodes from the size which gives you O(logN)
# time!

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.right = None
        self.left = None
        self.leftSize = 0

class BinaryTree:
    def __init__(self):
        self.root = None
        self.num = 0

    def insert(self, val):
        # insersts like a binary tree does O(logN)
        return

    def find(self, val):
        # uses binary search O(logN)
        return

    def delete(self, val):
        # uses binary serach to find node, bumps up a child to take its place
        # bump up smaller child, the add the larger child to the right most spot
        # of the smaller child's tree
        # O(logN + c) = O(logN)
        return

    def getRandomNode(self):
        # gets a random number between 0 and num, then traverses the tree
        # using the same find strategy until it lands on that node
        # O(n)
        # how many left children for each node?
        # so then you keep track of total ammount and you can pick a random
        # number and traverse and find it in O(logN) time, but it require O(N)
        # extra space
        return
