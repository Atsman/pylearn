"""
The parity of a sequence is 1 if the number of 1s in the
sequence is odd; otherwise, it is 0.
"""


def parity_bruteforce(x):
    bx = bin(x)
    count = 0
    for x in bx[2:]:
        if x == '1':
            count += 1

    if count % 2 != 0:
        return 1
    else:
        return 0


def parity_xor(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result
