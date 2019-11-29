# List of Depths: Given a binary tree, design an algorithm which creates a
# linked list of all nodes at each depth

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def getListOfLinkedLists(node, lists, depth):
    if (node.left is not None):
        lists = getListOfLinkedLists(node.left, lists, depth + 1)
    if (node.right is not None):
        lists = getListOfLinkedLists(node.right, lists, depth + 1)

    if (depth > len(lists) - 1):
        lists = lists + ([None] * (depth - len(lists) + 1))

    frontNode = lists[depth]
    node.left = None
    node.right = frontNode
    lists[depth] = node



    return lists

if __name__ == "__main__":
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    node.right.left = Node(6)
    node.right.right = Node(7)
    ll = getListOfLinkedLists(node, [], 0)
    for l in ll:
        curr = l
        while curr is not None:
            print(curr.val, end=" -> ")
            curr = curr.right
        print("None")
