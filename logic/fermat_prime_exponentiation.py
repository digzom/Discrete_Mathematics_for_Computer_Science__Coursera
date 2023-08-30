def is_prime(n):
    assert n > 0
    if n == 1:
        return False

    for d in range(2, n):
        if n % d == 0:
            return n

    return n


for n in range(0, 10):
    result = is_prime((2 ** (2 ** n)) + 1)
    if result:
        print(f'(2 ^ (2 ^ {n})) + 1 = {result}')