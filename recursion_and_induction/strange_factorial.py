def strange(n, k): 
    if n == k: 
        return k
    return n * strange(n + 1, k)

print(strange(1, 10))