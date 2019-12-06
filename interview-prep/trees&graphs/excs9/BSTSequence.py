# BST Sequences: A binary search tree was created by traversing through an array
# from left to right and inserting each element. Given a binary search tree with
# distinct elements, print all possible arrays that could have led to this tree.


# so root is always
# then it could be left then right?
# then it could be left.left or left.right or right.left or right.right?
# so its just all possible premutations at each level?

# but like the next level: like left.left could have came before right?
# this is so many
# so what cases cant exist?
# => parents must come before children
# =>

# node
# couldBeNext
#
# if (coudlBeNext.isNotEmpty)
#     next= couldBeNext.pop

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def BSTSequences(node):
    pf = []
    if (node.left is not None):
        pf.append(node.left)
    if (node.right is not None):
        pf.append(node.left)

    BSTSequencesHelper([node], pf)

def BSTSequencesHelper(prevOrder, possibleFuture):
    if (len(possibleFuture) != 0):
        for node in possibleFuture:
            newPossibleFuture = possibleFuture[:]
            newPossibleFuture.remove(node)
            if node.left is not None:
                newPossibleFuture.append(node.left)
            if node.right is not None:
                newPossibleFuture.append(node.right)
            BSTSequencesHelper(prevOrder + [node], newPossibleFuture)
    else:
        print("{ ", end="")
        for x in prevOrder:
            print(x.val, end=" ")
        print("}")

if __name__ == "__main__":
        node = Node(8)
        node.left = Node(4)
        node.left.left = Node(2)
        # node.left.left.left = Node(1)
        # node.left.left.right = Node(3)
        # node.left.right = Node(6)
        # node.left.right.left = Node(5)
        # node.left.right.right = Node(7)
        node.right = Node(12)
        # node.right.left = Node(10)
        # node.right.left.left = Node(9)
        # node.right.left.right = Node(11)
        # node.right.right = Node(14)
        # node.right.right.left = Node(13)
        # node.right.right.right = Node(15)
        BSTSequencesHelper([node], [node.left, node.right])
