class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def char_count(self, input):
        char_map = {}
        for i in range(len(input)):
            if input[i] in char_map:
                char_map[input[i]] += 1
            else:
                char_map[input[i]] = 1
        result = []
        for k in sorted(char_map.keys()):
            result += [k, str(char_map[k])]
        # return result
        return "".join(result)

    def anagrams(self, strs):
        anagram_map = {}
        result = []
        for i in range(len(strs)):
            char_count = self.char_count(strs[i])
            if char_count in anagram_map:
                anagram_map[char_count].append(i)
            else:
                anagram_map[char_count] = [i]
        for k in anagram_map.keys():
            arr = anagram_map[k]
            if len(arr) > 1:
                for i in range(len(arr)):
                    result.append(strs[anagram_map[k][i]])
        return result

s = Solution()
print s.anagrams(['cat', 'tac', 'dog', 'god', 'att'])
