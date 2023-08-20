
base_cases = {8: [3, 5], 9: [3, 3, 3], 10: [5, 5]}


def is_smaller_than(number, array):
    return any(number < num for num in array)


def change(amount):
    lista = list(base_cases.keys())

    if amount <= 10:
        return base_cases[amount]
    if is_smaller_than(amount - 5, lista):
        return change(amount - 3) + [3]

    return change(amount - 5) + [5]


print(change(18))
