def merge_sort(arr):
  result = []
  mid = len(arr)/2
  if len(arr) < 2:
    return arr
  left_half = merge_sort(arr[:mid])
  right_half = merge_sort(arr[mid:])
  i = 0
  j = 0

  while i < len(left_half) and j < len(right_half):
    if left_half[i] > right_half[j]:
      result.append(right_half[j])
      j += 1
    else:
      result.append(left_half[i])
      i += 1
  result += left_half[i:]
  result += right_half[j:]
  return result

def merge_sort2(items):
  """ Implementation of mergesort """
  if len(items) > 1:

    mid = len(items) / 2        # Determine the midpoint and split
    left = items[0:mid]
    right = items[mid:]

    merge_sort2(left)            # Sort left list in-place
    merge_sort2(right)           # Sort right list in-place

    l, r = 0, 0
    for i in range(len(items)):     # Merging the left and right list

      lval = left[l] if l < len(left) else None
      rval = right[r] if r < len(right) else None

      if (lval and rval and lval < rval) or rval is None:
        items[i] = lval
        l += 1
      elif (lval and rval and lval >= rval) or lval is None:
        items[i] = rval
        r += 1
      else:
        raise Exception('Could not merge, sub arrays sizes do not match the main array')


def insertion_sort(items):
  """ Implementation of insertion sort """
  for i in range(1, len(items)):
    j = i
    while j > 0 and items[j] < items[j-1]:
      items[j], items[j-1] = items[j-1], items[j]
      j -= 1

random_items = [9, 6, 3, 7, 8, 1, 2, 5]
# print 'Before: ', random_items
# insertion_sort(random_items)
# print 'After : ', random_items

print 'Before: ', random_items
merge_sort2(random_items)
print 'After : ', random_items
