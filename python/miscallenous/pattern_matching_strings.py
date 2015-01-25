# Given a pattern and a string input - find if  string follows the same pattern and return 0 or 1.
# Examples: 1) Pattern : "abba", input: "redblueredblue" should return 1.
# 2) Pattern: "aaaa", input: "asdasdasdasd" should return 1.
# 3) Pattern: "aabb", input: "xyzabcxzyabc" should return 0.

def matches_pattern(pattern, strinput, maps=None, pindex=0, sindex=0):

  if maps is None:
    maps = {}

  print maps
  print strinput

  if pindex == len(pattern) and sindex == len(strinput):
    return False
  if pindex == len(pattern) or sindex == len(strinput):
    return False

  if pattern[pindex] not in maps:
    maps[pattern[pindex]] = strinput[:sindex+1]
  else:
    return matches_pattern(pattern[pindex+1:], strinput[sindex+1:], maps, pindex + 1, sindex + 1)


print matches_pattern("abab", "redblueredblue")

