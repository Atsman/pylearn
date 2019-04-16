def rearrange(xs, i):
    """
    Rearrenges the elements such that all elements
    less than xs[i] appear first, followed by elements
    equal to xs[i], followed by elements greater than xs[i].

    Time complexity: O(N)
    Space complexity: O(1)
    """

    x = xs[i]
    p, q, r = 0, 0, len(xs) - 1
    # elements less then the pivot xs[0:p]
    # elements equal to the pivot xs[p:q]
    # elements that are unclassified xs[q:r+1]
    # elements greater then the pivot xs[r+1:len(xs)]
    while q <= r:
        if xs[q] < x:
            xs[q], xs[p] = xs[p], xs[q]
            p += 1
            q += 1
        elif xs[q] > x:
            xs[q], xs[r] = xs[r], xs[q]
            r -= 1
        elif xs[q] == x:
            q += 1
