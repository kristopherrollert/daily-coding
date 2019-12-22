# Insertion: You are given two 32-bit number, N and M, and two bit positions, i
# and j. Write a method to insert M into N such that M starts at bit j and ends
# at bit i. You can assume that the nits j through i have enough space to fit
# all of M.

def insertion(M, N, i, j):
    mask = (1 << (j - i)) - 1
    mask = ~(mask << i)
    M = M & mask
    M = M | (N << i)
    print(bin(M))

insertion(0b10000000000, 0b10011, 2, 6)
