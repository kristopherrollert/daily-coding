# Triple Step: A child is running up a staircase with n steps and can hop either
# 1, 2, or 3 steps at a time. Implement a mehtod to count how many possible ways
# the child can run up the stairs.

def tripleStep(stepsLeft, dict):
    if (stepsLeft in dict):
        return dict[stepsLeft]
    elif (stepsLeft >= 1):
        total = 0
        total += tripleStep(stepsLeft - 1, dict)
        if (stepsLeft >= 2):
            total += tripleStep(stepsLeft - 2, dict)
            if (stepsLeft >= 3):
                total += tripleStep(stepsLeft - 3, dict)
        dict[stepsLeft] = total
        return total
    else:
        return 1

print(tripleStep(3, {}))
