# Successor: Write an algorithm to find the "next" node, (i.e. the in-order
# successor) of a given node in a binary search tree. You may assume that each
# node has a link to it's parent

class Node:
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None

def successor(node):

    if (node.right is None):
        prev = node
        curr = node.parent
        while (curr is not None and curr.left != prev):
            prev = curr
            curr = curr.parent

        return curr
    else:
        prev = node.right
        curr = prev.left
        while (curr is not None):
            prev = curr
            curr = curr.left

        return prev


def validateBST(node, minVal, maxVal):
    print(node.val)
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
    node8 = Node(8, None)

    # left tree
    node4 = Node(4, node8)
    node8.left = node4

    node2 = Node(2, node4)
    node4.left = node2

    node6 = Node(6, node4)
    node4.right = node6

    node5 = Node(5, node6)
    node6.left = node5

    node7 = Node(7, node6)
    node6.right = node7

    node1 = Node(1, node2)
    node2.left = node1

    node3 = Node(3, node2)
    node2.right = node3

    # right tree
    node12 = Node(12, node8)
    node8.right = node12

    node10 = Node(10, node12)
    node12.left = node10

    node14 = Node(14, node12)
    node12.right = node14

    node9 = Node(9, node10)
    node10.left = node9

    node11 = Node(11, node10)
    node10.right = node11

    node14 = Node(14, node12)
    node12.right = node14

    node13 = Node(13, node14)
    node14.left = node13

    node15 = Node(15, node14)
    node14.right = node15

    print(successor(node14).val)
