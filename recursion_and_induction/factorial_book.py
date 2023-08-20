def factorial(n):
    assert n > 0
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result

print(factorial(2000))