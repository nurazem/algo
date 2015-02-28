def max_subarray(arr):
  temp_sum = 0
  max_sum = 0
  for i in range(len(arr)):
    temp_sum += arr[i]
    if temp_sum < 0:
      temp_sum = 0
    if max_sum < temp_sum:
      max_sum = temp_sum
  return max_sum

print max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
