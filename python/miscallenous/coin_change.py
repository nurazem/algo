def coin_change(n, coins):
  queue = list(coins)
  result = 0
  while queue != []:
    print queue
    current = queue.pop(0)
    print 'current ' + str(current)
    for c in coins:
      if current + c == n:
        result += 1
        print 'incrementing ' + str(result)
      elif current + c < n:
        print 'appending ' + str(current + c)
        queue.append(current + c)
  return result

def coin_change_rec(n, coins):
  if n == 0:
    return 1
  if n < 0:
    return 0
  if len(coins) == 0 and n >= 1:
    return 0
  print (n, coins[:len(coins) - 1])
  print (n - coins[-1], coins)
  return coin_change_rec(n, coins[:len(coins) - 1]) + coin_change_rec(n - coins[-1], coins)

# print coin_change_rec(4, [1, 2, 3])
print coin_change_rec(10, [2, 3, 5, 6])
