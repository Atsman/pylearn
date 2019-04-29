def run_length_encoding(text):
    """
    Efficiemt on the fly compression and decompression
    of the string.

    Encodes successive repeated characters by repetiting 
    count and the character.

    Example: aaaaabbcccaa -> 4a2b3c2a

    Time complexity: O(N)
    Space complexity: O(N)
    """

    current_ch = text[0]
    count = 0
    buf = []
    for ch in text:
        if ch != current_ch:
            buf.append(str(count))
            buf.append(current_ch)
            count = 0
            current_ch = ch

        count += 1

    buf.append(str(count))
    buf.append(current_ch)

    return "".join(buf)
