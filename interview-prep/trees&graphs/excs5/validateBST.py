# Validate BST: Implement a function to check if a binary is a binary search
# tree.


# bst property: every node left is smaller
# hard to check recursively because what about multiple levels

# so like parent val maybe? then you check that children are less if left and
# greater if equal, but the biggest shouldn't be larger than the parent

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def validateBST(node, minVal, maxVal):
    if minVal is not None and minVal > node.val: return False
    if maxVal is not None and maxVal < node.val: return False

    if (node.left is not None):
        ok = validateBST(node.left, minVal, node.val)
        if not ok: return False

    if (node.right is not None):
        ok = validateBST(node.right, node.val, maxVal)
        if not ok: return False

    return True


if __name__ == "__main__":
    node = Node(8)
    node.left = Node(4)
    node.left.left = Node(2)
    node.left.left.left = Node(1)
    node.left.left.right = Node(3)
    node.left.right = Node(6)
    node.left.right.left = Node(5)
    node.left.right.right = Node(9)
    node.right = Node(15)
    node.right.left = Node(10)
    node.right.left.left = Node(9)
    node.right.left.right = Node(11)
    node.right.right = Node(17)
    node.right.right.left = Node(16)
    node.right.right.right = Node(18)
    print(validateBST(node, None, None))
