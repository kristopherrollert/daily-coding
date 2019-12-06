# set up linked lists from root to node1 and node2
# then you can traverse the linked lists and compare elements till they match
# don't match, then the previous was the most in common.

# how do you make these linked lists.
# traversal. left then right. If none pop off of linked list.
# how about binary instead? left is 0 right is 1?

from stack import *

LEFT = 0
RIGHT = 1

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def firstCommonAncestor1(root, node1, node2):
    if (root == node1 or root == node2):
        return root

    found1 = False
    found2 = False
    path1 = None
    path2 = None
    parentPath = Stack()
    parentPath.push([root, LEFT])
    curr = root.left
    while (True):
        if (curr == node1):
            found1 = True
            path1 = parentPath.toList()
            if (found2): break

        if (curr == node2):
            found2 = True
            path2 = parentPath.toList()
            if (found1): break

        if (curr.left is not None):
            parentPath.push([curr, LEFT])
            curr = curr.left
        elif (curr.right is not None):
            parentPath.push([curr, RIGHT])
            curr = curr.right
        else:
            [curr, way] = parentPath.pop()
            while (way == RIGHT):
                [curr, way] = parentPath.pop()

            parentPath.push([curr, RIGHT])
            curr = curr.right

    min = len(path1) if len(path1) < len(path2) else len(path2)
    prev = root
    for i in range(min - 1, -1, -1):
        if (path1[i] != path2[i]):
            return prev
        prev = path1[i]
    return path1[min]


# not optimal, but close
# I am using the books answer. once you've found the first, then keep
# track of highest node you went right with. That's
def firstCommonAncestor2(root, node1, node2):
    if (root == node1 or root == node2):
        return root

    found1 = False
    found2 = False
    parentPath = Stack()
    parentPath.push([root, LEFT])
    curr = root.left
    depth = 0

    pivotDepth = None
    pivot = None
    while (True):
        if (curr == node1):
            if (found2): break
            found1 = True

        if (curr == node2):
            if (found1): break
            found2 = True

        if (curr.left is not None):
            depth += 1
            parentPath.push([curr, LEFT])
            curr = curr.left
        elif (curr.right is not None):
            depth += 1
            parentPath.push([curr, RIGHT])
            curr = curr.right
        else:
            [curr, way] = parentPath.pop()
            while (way == RIGHT):
                depth -= 1
                [curr, way] = parentPath.pop()

            if (found1 or found2):
                if (pivotDepth is None or depth < pivotDepth):
                    print("setting as", curr.val)
                    pivot = curr
                    pivotDepth = depth

                if depth == 0:
                    break

            parentPath.push([curr, RIGHT])
            curr = curr.right

    return pivot


if __name__ == "__main__":
    node = Node(8)
    node.left = Node(4)
    node.left.left = Node(2)
    node.left.left.left = Node(1)
    node.left.left.right = Node(3)
    node.left.right = Node(6)
    node.left.right.left = Node(5)
    c = Node(7)
    node.left.right.right = c
    node.right = Node(12)
    node.right.left = Node(10)
    node.right.left.left = Node(9)
    a = Node(11)
    node.right.left.right = a
    node.right.right = Node(14)
    b = Node(13)
    node.right.right.left = b
    node.right.right.right = Node(15)

    print(firstCommonAncestor2(node, a, b).val)
