def magic_index(arr, start=None, end=None):
  if start == None:
    start = 0
  if end == None:
    end = len(arr) - 1
  if start > end or end > len(arr) - 1 or start < 0:
    return -1
  mid = (end + start) / 2
  # print mid
  if arr[mid] == mid + 1:
    return mid + 1
  elif arr[mid] < mid + 1:
    return magic_index(arr, mid, end)
  else:
    return magic_index(arr, 0, mid)

print magic_index([-40, -20, -1, 1, 2, 3, 5, 8, 9, 12, 13])
