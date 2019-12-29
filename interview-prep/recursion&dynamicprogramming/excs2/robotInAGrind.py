# Robot in a Grind: Imagine a robot sitting on the upper left conrner of grid
# with r rows and c columns. The robot can only move in two directions, right
# and down, but certain cells are "off limits" such that the robot cannot step
# on them. Design an algorithm to find a path for the robot from the top left to
# the bottom right.

def robotInAGrind(rows, columns, invalidSquaresList):
    return helper({}, 0, 0, invalidSquaresList, rows -1, columns -1)


# the idea: recursively run down and right. But if you get to a sqare that
# you've already checked before, don't go there! If you get back down and right
# both didn't work out, then update checked to return false. If either worked,
# return true and pass it back up the chain!
def helper(checked, currR, currC, invalidSquaresList, endR, endC):
    if (currR == endR and currC == endC):
        return [[currR, currC], [endR, endC]]

    if currR + 1 <= endR and [currR + 1, currC] not in invalidSquaresList and \
        not ((currR + 1) in checked and currC in checked[currR]):
        path = helper(checked, currR + 1, currC, invalidSquaresList, endR, endC)
        if (path): return [[currR, currC]] + path

    if currC + 1 <= endC and [currR, currC + 1] not in invalidSquaresList and \
        not (currR in checked and (currC + 1) in checked[currR]):
        path = helper(checked, currR, currC + 1, invalidSquaresList, endR, endC)
        if (path): return [[currR, currC]] + path

    if currR not in checked:
        checked[currR] = {currC: False}
    else:
        checked[currR][currC] = False

    return False


print(robotInAGrind(5, 5, [[1,0], [1, 1], [1, 2], [1, 3]]))
