def guess(lower: int, upper: int):
  middle = (lower + upper) // 2

  answer = input(f'Is x = {middle}? (equal, smaller, greater) \n')

  if answer == 'equal':
    print("Thanks for playing!")
    return
  elif answer == 'smaller':
    guess(lower, middle - 1)
  elif answer == 'greater': 
    guess(middle + 1, upper)
  else:
    print('Not supported answer.')
    guess(lower, upper)


print('Decida o intervalo entre os números para que eu tente adivinhar o mais rápido possível: \n')

lower = int(input('Menor número: '))
upper = int(input('Maior número: '))

guess(lower, upper)