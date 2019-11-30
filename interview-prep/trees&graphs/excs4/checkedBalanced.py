# Check Balanced: Implement a function to check if a binary tree is balanced.
# For the purpose of this question, a balanced tree is defined to be a tree such
# that the heights of the two subtrees of any node never differs by more than one

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def isBalanced(node):
    if (node is None):
        return 0, True
    sum1, isB1 = isBalanced(node.left)
    sum2, isB2 = isBalanced(node.right)

    if (not isB1 or not isB2):
        return 0, False

    if (abs(sum1 - sum2) < 2):
        return sum1 + sum2 + 1, True
    return 0, False


if __name__ == "__main__":
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    # node.right.left = Node(6)
    # node.right.right = Node(7)
    print(isBalanced(node))
