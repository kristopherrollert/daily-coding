# PairwiseSwap: Write a program to swap odd and even bits in an integer with as
# few instructions as possible (e.g., bit 9 and bit 1 are swapped, bit 2 and
# bit 3 are swapped, and so on)


# Brute force: keep bit shifting by 2, AND the number with 3 (11), use the
# table above to swap the bits, then shift it over by and OR it with the new
# number
# This isn't fast. It takes an increasing amount of shifts as you grab each bit
# switching bits isn't too fast either


def pairwiseSwap(A):
    new = 0
    i = 0
    while (A != 0):
        B = A & 3
        B = getFlipped(B)
        new = new | (B << i)
        A >>= 2
        i += 2
    return new

def getFlipped(B):
    if (B == 0 or B == 3):
        return B
    elif (B == 1):
        return 2
    return 1

# New Idea using hints
# getting just the even bits : & (101010) then >> 1
# getting just the odd bits  : & (010101) then << 1
# then & both numbers?
# it is hard to create a 1010101 number
# 0ABCD => BADC
# ABCD0
# 00ABC
def pairwiseSwap2(A):
    m = 0xAAAAAAAA
    n = 0x55555555
    return (m & (A << 1)) | (n & (A >> 1)))

pairwiseSwap2(0b0111)
