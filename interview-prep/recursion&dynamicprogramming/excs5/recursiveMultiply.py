# Recrusive Multiply: Write a recursive function to multiply two positive
# integers without using the * operator. You can use addition, subtraction,
# and bit shifting but you should minimize the number of those operations


# O(b)
def mult(a, b):
    [a, b] = [a,b] if a < b else [b, a]
    product = 0
    for i in range(0, a):
        product += b
    return product

def mult2(a, b):
    d = 1
    while (a % 2 == 0):
        d <<= 1
        a /= 2

    while (b % 2 == 0):
        d <<= 1
        b /= 2

    [a, b] = [a,b] if a < b else [b, a]
    product = 0
    for i in range(0, int(a)):
        product += b
    return product * d


print(mult2(10, 143))
