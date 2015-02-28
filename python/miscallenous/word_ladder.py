# class Solution:
#     # @param start, a string
#     # @param end, a string
#     # @param dict, a set of string
#     # @return an integer

#     def letterChanger(self, word):
#         a = ord('a')
#         z = ord('z')
#         result = []
#         for i in range(len(word)):
#             for l in range(a, z + 1):
#                 if chr(l) != word[i]:
#                     current = word
#                     current = word[:i] + chr(l) + word[i + 1:]
#                     result.append(current)
#         return result

#     def ladderLength(self, start, end, dictionary):
#         shortest_path_len = 0
#         current_words = [start]
#         visited = {}
#         while len(current_words) != 0:
#             current = current_words.pop()
#             # print current
#             if current in dictionary and current not in visited:
#                 visited[current] = True
#                 print current
#                 if current == end:
#                     return shortest_path_len
#                 else:
#                     current_words = self.letterChanger(current)
#                     shortest_path_len += 1
        # return shortest_path_len

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string!!!dict is a set type!!!
    # @return an integer
    def ladderLength(self, start, end, dictionary):
        dictionary.append(end)
        q = []
        q.append((start, 1))
        while q:
            curr = q.pop(0)
            currword = curr[0]; currlen = curr[1]
            if currword == end: return currlen
            for i in range(len(start)):
                part1 = currword[:i]; part2 = currword[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currword[i] != j:
                        nextword = part1 + j + part2
                        if nextword in dictionary:
                            q.append((nextword, currlen+1));
                            dictionary.remove(nextword)
        return 0


print Solution().ladderLength('a', 'c', ['a', 'b', 'c'])
print Solution().ladderLength("hot", "dog", ["hot","dog","dot"])
print Solution().ladderLength("hot", "dog", ["hot","dog"])
# print Solution().letterChanger('a')
