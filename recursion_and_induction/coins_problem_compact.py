base_cases = {8: [3, 5], 9: [3, 3, 3], 10: [5, 5]}


def change(amount):
    if amount <= 10:
        return base_cases[amount]

    return change(amount - 3) + [3]

print(change(15))