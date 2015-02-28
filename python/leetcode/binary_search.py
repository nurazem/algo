def binary_search(arr, e):
  mid = len(arr) / 2
  if arr[mid] == e:
    return mid
  elif arr[mid] < e:
    print arr[mid+1:]
    return binary_search(arr[mid+1:], e) + mid
  else:
    return binary_search(arr[:mid], e)

print binary_search([1, 2, 3, 4, 5, 6], 4)
