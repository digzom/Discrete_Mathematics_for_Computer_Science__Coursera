def extend(perm, n):
    if len(perm) == n:
        print(f'Final permutation: {perm}')
        return

    print(f'Extending partial permutation {perm}...')
    for k in range(n):
        if k not in perm:
            extend(perm + [k], n)


extend(perm=[], n=3)
