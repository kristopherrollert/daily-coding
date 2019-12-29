# Magic Index: a magic index is an array A[0...n-1] is defined to be an index
# such that A[i] = i. Given a sorted array of distinct integers, write a method
# to find a magic index, if one exists, in Array A.

# So here is my idea. You go in the middle. There are three options.
# 1. the middle is the magic index (woo!) you're done
# 2. the index of the middle is larger than the middle number. This means that
#    there is no way the left side of the array can equal the index. So check
#    the right
# 3. the index in the middle is smaller than the middle number. There is no way
#    the right side of the array can work.
#  [-2,-1,0,1,4,8,]
#    0  1 2 3 4 5


import math
def magicIndex(arr):
    return helper(0, len(arr) -1, arr)

def helper(start, end, arr):
    if (start > end):
        return False

    i = (start + end) // 2
    if (i == arr[i]):
        return True
    elif (i < arr[i]):
        return helper(start, i - 1, arr)
    else:
        return helper(i + 1, end, arr)


print(magicIndex([-2, -1, 0, 1, 7, 8]))

# FOLLOWUP: What if the values are not distinct?
# you cannot use the exact same method because the function is not always
# increasing the same properties hold
# This way you must just traverse the array in O(n) time


# WRONG - this is what the book says. We can't do the same, but we can reduce
# the amount of searches by leveraging that if i != arr[i], then we can skip
# all the values from i to arr[i - 1] because they couldn't be equal to there
# value


def helper2(start, end, arr):
    if (start > end):
        return False

    i = (start + end) // 2
    if (i == arr[i]):
        return True

    leftIndex = math.min(i-1, arr[i])
    ok = helper(start, leftIndex, arr)
    if (ok) return ok

    rightIndex = math.min(arr[i], i + 1)
    return helper(rightIndex, end, arr)
