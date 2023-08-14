def can_be_extended(perm):
    i = len(perm) - 1
    return all(i - j != abs(perm[i] - perm[j]) for j in range(i))


def extend(perm, n):
    if len(perm) == n:
        print(perm)
        exit()

    for k in range(n):
        if k not in perm:
            if can_be_extended(perm + [k]):
                extend(perm + [k], n)


extend(perm=[], n=24)
