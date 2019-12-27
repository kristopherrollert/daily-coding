# Conversion: Write a function to determine the number of bits you would need
# to flip to convert integer A to integer B

# brute force, traverse bits O(N) counting different bits
# not Xor ~ (A ^ B)


def conversion(A, B):
    C = A ^ B
    total = 0
    while (C != 0):
        total += C & 1
        C >>= 1
    return total

print(conversion(29, 15))
