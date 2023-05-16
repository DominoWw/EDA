def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices for x. If
    x does not exist return -1, -1."""
    if a is None or len(a) == 0:
        return -1, -1
    return _find_first_last(a, x, 0, len(a) - 1)

def _find_first_last(a: list, x: int, start: int, end: int) -> (int, int):
    """returns the index of the first occurrence of x in a,
    and the index of the last occurrence of x in a."""
    # if start > end:  it is not necessary
    #    return -1, -1

    if start == end:
        if a[start] == x:
            return start, start
        return -1, -1

    if start < end:
        m = (start + end) // 2
        first_1, last_1 = _find_first_last(a, x, start, m)
        first_2, last_2 = _find_first_last(a, x, m+1, end)

        first = first_2 if first_1 == -1 else first_1
        last = last_1 if last_2 == -1 else last_2

        return first, last

import random

if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # no existe
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
