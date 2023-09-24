from itertools import product

for number, password in enumerate(product('abcdefghijklmnopqrstuvwxyz', repeat=5)):
    print(number, ''.join(password))
