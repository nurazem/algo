class Solution:
    # @return a string
    def convert(self, s, nRows):
        result = ''
        i = 0
        if nRows == 1:
            return s
        while i < nRows:
            j = i
            if i == nRows/2:
                while j < len(s):
                    result += s[j]
                    print j
                    j += (nRows/2 + 1)
            else:
                while j < len(s):
                    result += s[j]
                    j += (nRows + 1)

            i += 1
        return result

s = Solution()
print s.convert('ABC', 2)
