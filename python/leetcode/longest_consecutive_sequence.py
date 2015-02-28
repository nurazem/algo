class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        result = 0
        hash = {}
        for i in range(len(num)):
            hash[num[i]] = True

        for i in range(len(num)):
            current = num[i]
            cur_length = 1
            while (current+1) in hash:
                cur_length += 1
                current += 1
            result = max(result, cur_length)
        return result

s = Solution()
print s.longestConsecutive([1, 2, 3, 4])
