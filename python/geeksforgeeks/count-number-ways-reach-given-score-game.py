def number_of_ways(n, s=None):
  if s == None: s = 0
  print s
  if s > n:
    return 0
  if s == n:
    return 1

  return number_of_ways(n, s + 3) + number_of_ways(n, s + 5) + number_of_ways(n, s +  10)

def number_of_ways_with_table(n):
  table = [0] * (n + 1)
  table[0] = 1
  for i in range(3, n + 1):
    table[i] += table[i - 3]
  for i in range(5, n + 1):
    table[i] += table[i - 5]
  for i in range(10, n + 1):
    table[i] += table[i - 10]
  return table

# print number_of_ways(13)
print number_of_ways_with_table(20)
