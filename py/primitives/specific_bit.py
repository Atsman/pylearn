def specific_bit(number, position, bit):
    """
    Modifies a bit at a given position in number.

    Example:
    x = 0b0011, p = 2, b = 0
    r = 0b0001

    Time and space complexity: O(1)
    """
    mask = 1 << position
    return (number & ~mask) | bit << position
