def matches_pattern(pattern, input, maps=None):
  if maps == None: maps = {}
  if len(pattern) == 1:
    return maps[pattern[0]] == input
  i = 1
  while len(pattern) != 0 or i < len(input):
    print pattern
    p = pattern.pop()
    if p in maps:
      current = maps[p]
      print current
      if is_prefix(current, input):
        print (pattern, input[len(current):])
        matches_pattern(pattern, input[len(current):], maps)
    else:
      match = input[:i]
      print match
      maps[p] = match
      matches_pattern(pattern, input[i:], maps)

    i += 1

  return False


def matches_pattern_rec(pattern, input, i_backup=None, maps=None, n=None, p=None):
  if maps == None: maps = {}
  if i_backup == None: i_backup = str(input)
  if n == None: n = 1
  if p == None: p = 0
  print (p, input, maps)
  if p == len(pattern) - 1:
    return maps[pattern[-1]] == input

  pat = pattern[p]
  match = input[:n]
  print (pat, match)
  if pat in maps:
    if is_prefix(maps[pat], input):
      return matches_pattern_rec(pattern, input[len(maps[pat]):], i_backup, maps, n, p + 1)
    else:
      print n
      return matches_pattern_rec(pattern, i_backup, i_backup, None, n + 1, 0)
  else:
    maps[pat] = match
    return matches_pattern_rec(pattern, input[n:], i_backup, maps, n, p + 1)

def is_prefix(a, s):
  if len(a) > len(s):
    return False
  for i in range(len(a)):
    if a[i] != s[i]:
      return False
  return True

# print is_prefix('abc', 'abcfee')

# print matches_pattern_rec('abab', 'xyzabcxyzabc')
print matches_pattern_rec('abccba', 'redblugregreblured')
# print matches_pattern_rec('aaaa', 'asdasdasdasd')
# print matches_pattern(['a', 'a', 'b' , 'b'], 'xyzabcxzyabc')
