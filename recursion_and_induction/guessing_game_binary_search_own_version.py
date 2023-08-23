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
    guess(lower, upper)



guess(1, 10)