def foo(n):
  assert n >= 0
  if n == 0:
    return 0
  else:
    return foo(n - 1) + 2

print(foo(2))