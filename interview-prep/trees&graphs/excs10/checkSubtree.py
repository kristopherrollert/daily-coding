# Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger
# than T2. Create an algorithm to determine if T2 is a subtree of T1

# Notes:
# so maybe we search for node. Then once we have found the root we traverse?

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def checkSubtree(rootT1, rootT2):
    s = Stack()
    curr = rootT1
    while (True):
        if (curr is not None):
            s.push(curr)
            curr = curr.left
        elif (not s2.isEmpty()):
            curr = s.pop()
            if (curr.val == rootT2.val):
                if (checkMatch(curr, rootT2)):
                    return True
            curr = curr.right
        else:
            break
    return False

def checkMatch(rootT1, rootT2):
    s1 = Stack()
    s2 = Stack()
    curr1 = rootT1
    curr2 = rootT2
    while (True):
        if curr1.val != curr2.val:
            return False

        if (curr2 is not None):
            s2.push(curr2)
            curr2 = curr2.left
        elif (not stack.isEmpty()):
            curr2 = s.pop()
            curr2 = curr2.right
        else:
            return s1.isEmpty();

        if (curr1 is not None):
            s1.push(curr1)
            curr1 = curr1.left
        elif (not s1.isEmpty()):
            curr1 = s.pop()
            curr1 = curr1.right
        else:
            return s2.isEmpty();
