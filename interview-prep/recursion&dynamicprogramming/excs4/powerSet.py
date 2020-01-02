# Power Set: Write a method to return all subsets of a set

import math

def powerSet(set):
    ps = [[]]
    for i in range(len(set)):
        ps += helper(set, i)
    return ps
# go by level?
#

# power set - set of all sets
# [1,2,3] 1, 2, 3 // 12, 13, 23 // 123
def helper(lst, size):
    # if size == 0:
    #     return []

    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []
    for i in range(len(lst)):
        m = lst[i]
        remaining = lst[:i] + lst[i+1:]
        for p in helper(lst, size -1):
            l.append([m] + p)

    return l


def powerSet2(lst):
    m = int(math.pow(2, len(lst)))
    n = []
    for x in range(0, m):
        n += [helper2(x, lst)]
    return n

def helper2(x, lst):
    n = []
    i = 0
    while (x != 0):
        if x & 1 != 0:
            n.append(lst[i])
        i += 1
        x >>= 1
    return n

print(powerSet2([1,2,3]))

# we need to recursively create a new list. Start by traversing down to
# making lists of one, then return those lists. Then the next level
# creates all the lists possible by combining elements in the returned
# data with the elements in the list
