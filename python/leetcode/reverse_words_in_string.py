def reverse_words(s):
  result = ''
  j = len(s)
  for i in range(len(s) - 1, -1, -1):
    if s[i] == ' ':
      j = i
    elif i == 0 or s[i-1] == ' ':
      if len(result) != 0:
        result += ' '
      result += s[i:j]
  return result

print reverse_words('this is a blue sky')
