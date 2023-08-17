from typing import List

count = 0

def can_be_extended(perm):
    i = len(perm) - 1
    return all(i - j != abs(perm[i] - perm[j]) for j in range(i))

def extend(perm, n):
    global count
    if len(perm) == n:
        print(perm)
        count += 1

    for k in range(n):
        if k not in perm:
            if can_be_extended(perm + [k]):
                extend(perm + [k], n)
                
                
                


# I just need to pass the size of the board (in this case, is a 3x3 board) because
# our intent is to make a permutation thought all cells
extend(perm=[], n=8)
print(count)

