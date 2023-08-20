base_cases = {
    24: [5, 5, 7, 7],
    25: [5, 5, 5, 5, 5],
    26: [5, 7, 7, 7],
    27: [5, 5, 5, 5, 7],
    28: [7, 7, 7, 7],
}

def change(amount):
    if amount <= 28:
        return base_cases[amount]

    return change(amount - 5) + [5]

print(change(29))