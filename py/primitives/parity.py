"""
The parity of a sequence is 1 if the number of 1s in the
sequence is odd; otherwise, it is 0.
"""


def parity_bruteforce(x):
    """
    Returns 1 if the number of bits set to 1 in x is odd, otherwise 0.

    Time complexity O(N)
    Space complexity O(1)
    """
    bx = bin(x)
    count = 0
    for x in bx[2:]:
        if x == '1':
            count += 1

    if count % 2 != 0:
        return 1

    return 0


def parity_xor(x):
    """
    Returns 1 if the number of bits set to 1 in x is odd, otherwise 0.

    Time complexity O(K) where K is the number of bits in x set to 1.
    Space compexity O(1)
    """
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result
