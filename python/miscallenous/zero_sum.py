# Given an array of integers eg [1,2,-3,1]
# find whether there is a sub-sequence that sums to 0 and return it, continuous
# (eg 1,2,-3 or 2,-3,1)
def zero_sum_exists(A):
  maps = {}
  current_sum = 0
  result = []
  for i in range(len(A)):
    current_sum += A[i]
    if current_sum == 0:
      result.append(A[:i+1])
    elif current_sum in maps:
      result.append(A[maps[current_sum]+1:i+1])
    else:
      maps[current_sum] = i
  return result


print zero_sum_exists([1,2,-3,1])
