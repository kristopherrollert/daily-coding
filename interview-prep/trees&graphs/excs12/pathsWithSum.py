# Paths with Sum: You are given a binary tree in which each node contains an
# integer value (which might be positive or negative). Design an algorithm to
# count the number of paths that sum to a given value. The path does not need to
# start or end at the root or leaf, but it must go downwards (traveling only
# from parent nodes to child nodes).

# I have no idea how to solve this. Right now it seems like brute force is the
# move. Once again, they say binary tree but DONT say if it is a binary search
# tree. Sometimes when they say binary tree it is and sometimes it isn't it is
# annoying.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def pathsWithSum():
    a = Node(1)
    b = Node(-2)
    c = Node(4)
    d = Node(5)
    a.left = b
    a.right = c
    b.left = d
    succ = helper2(a, 5, 0, {})
    print(succ)


def helper(pastSum, node, succ, val, dict):
    if (pastSum + node.val == val):
        succ += 1


    if (node.left is not None):
        [succ, dict] = helper(pastSum + node.val, node.left, succ, val, dict)
        [succ, dict] = helper(0, node.left, succ, val, dict)

    if (node.right is not None):
        [succ, dict] = helper(pathSum + node.val, node.right, succ, val)
        [succ, dict] = helper(0, node.right, succ, val)

    return succ

def helper2(node, targetSum, runningSum, pathCount):
    if (node is None):
        return 0;

    runningSum += node.val
    sum = runningSum - targetSum
    totalPaths = pathCount.get(sum, 0)

    if (runningSum == targetSum):
        totalPaths += 1


    print(node.val, pathCount)
    inc(pathCount, runningSum, 1)
    totalPaths += helper2(node.left, targetSum, runningSum, pathCount)
    totalPaths += helper2(node.right, targetSum, runningSum, pathCount)
    inc(pathCount, runningSum, -1)

    return totalPaths


def inc(dict, key, delta):
    newCount = dict.get(key, 0) + delta
    if (newCount == 0):
        del dict[key]
    else:
        dict[key] = newCount


if __name__ == "__main__":
    pathsWithSum()
