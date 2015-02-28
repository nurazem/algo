def possible_steps(n, cache = None):
  if cache == None:
    cache = [None] * (n + 1)
  print n
  if n < 0:
    return 0
  elif n == 0:
    return 1
  elif cache[n] > - 1:
    return cache[n]
  else:
    cache[n] = possible_steps(n - 1, cache) + possible_steps(n -2, cache) + possible_steps(n - 3, cache)
    return cache[n]

print possible_steps(100)
