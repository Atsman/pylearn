"""
Modify a bit at a given position.

Example:

x = 0b0011
p = 2
b = 0

r = 0b0001
"""


def specific_bit(n, p, b):
    mask = 1 << p
    return (n & ~mask) | b << p
