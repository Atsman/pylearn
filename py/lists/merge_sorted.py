def merge_sorted(head1, head2):
    """
    Mergers two sorted linked lists. 

    Time complexity: O(N)
    Space complexity: O(1)
    """

    cn1 = head1
    cn2 = head2

    head = None
    if cn1.value <= cn2.value:
        head = cn1
    else:
        head = cn2

    while cn1 and cn2:
        if cn1.value > cn2.value:
            temp = cn2.next
            cn2.next = cn1
            cn2 = temp
        else:
            temp = cn1.next
            cn1.next = cn2
            cn1 = temp

    return head
