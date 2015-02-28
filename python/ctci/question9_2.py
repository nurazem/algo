def robot_paths(x, y):
  if x == 0 and y == 0:
    return 0
  elif y == 0:
    return 1
  elif x == 0:
    return 1
  else:
    return robot_paths(x - 1, y) + robot_paths(x, y - 1)

print robot_paths(2, 3)
