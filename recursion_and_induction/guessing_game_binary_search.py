def query(y: int):
  x = 100
  if x == y:
    return 'equal'
  elif x < y:
    return 'smaller'
  else:
    return 'greater'


def guess(lower: int, upper: int):
  middle = (lower + upper) // 2
  answer = query(middle)

  print(f'Is x = {middle}? It is {answer}')

  if answer == 'equal':
    return
  elif answer == 'smaller':
    guess(lower, middle - 1)
  else: 
    assert answer == 'greater'
    guess(middle + 1, upper)


guess(1, 100)