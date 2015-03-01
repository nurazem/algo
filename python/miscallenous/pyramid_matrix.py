def pyramidMatrix(n):
  m = [[None] * n for i in range(n)]
  current = 0
  i = 0
  while current <= n/2:
    while i < n - current:
      j = 0
      while j < n - current:
        print (n, current, i, j)
        if i == current or i == n - 1 - current or j == current or j == n - 1 - current:
          m[i][j] = current
        j += 1
      i += 1
      current += 1
    i, j = current, current
  return m


m = pyramidMatrix(5)
for el in m:
  print el
