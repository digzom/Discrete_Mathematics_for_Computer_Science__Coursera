from typing import List

def can_be_extended(perm: List) -> bool:
    i = len(perm) - 1
    return all(i - j != abs(perm[i] - perm[j]) for j in range(i))

def extend(perm: List[int], n: int):
    if len(perm) == n:
        print(perm)
        exit()

    for k in range(n):
        if k not in perm:
            if can_be_extended(perm + [k]):
                extend(perm + [k], n)


# I just need to pass the size of the board (in this case, is a 3x3 board) because
# our intent is to make a permutation thought all cells
extend(perm=[], n=24)
