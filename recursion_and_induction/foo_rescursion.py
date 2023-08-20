def foo(n): # 4 -> 3 -> 2 -> 1 -> 
  assert n >= 0 # true -> true -> true -> true -> true
  if n == 0: # false -> false -> false -> true
    return 0 # jump -> jump -> jump -> 0
  else:
    return foo(n - 1) + 2 # 6 + 2 = 8 -> 4 + 2 = 6 -> 2 + 2 = 4 

print(foo(2))