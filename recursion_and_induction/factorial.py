def factorial(n):
    if n == 0:
        return 1

    # this is like 4 * 3! which is equals to 4!
    return n * factorial(n - 1)


print(factorial(9))
# this is true
# y = 8
# print(factorial(y + 1) / (y + 1) == factorial(y))
