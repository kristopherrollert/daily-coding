# Power Set: Write a method to return all subsets of a set



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

print(powerSet([1,2,3]))
