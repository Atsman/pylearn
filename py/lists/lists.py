def max(xs):
    m = xs[0]
    for x in xs:
        if x > m:
            m = x
    return m


def min(xs):
    m = xs[0]
    for x in xs:
        if x < m:
            m = x
    return m


def sum(xs):
    s = 0
    for x in xs:
        s += x
    return s


def median(xs):
    xs.sort()

    l = len(xs) - 1

    middle = l // 2
    is_even = l % 2

    if is_even:
        return (xs[middle] + xs[middle + 1]) / 2

    return xs[middle]


def average(xs):
    s = sum(xs)
    return s / len(xs)
