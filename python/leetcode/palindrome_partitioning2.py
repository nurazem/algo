class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        if len(s) <= 1:
            return 0
        for i in range(len(s), -1, -1): # (l - 1, l - 2, ...0)
            if self.isPalindrome(s[:i + 1]) and i < len(s):
                print (s[:i + 1], s[i+1:])
                return self.minCut(s[i+1:]) + 1


    def isPalindrome(self, s):
        if len(s) == 0: return False
        for i in range(len(s) / 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True

# print Solution().isPalindrome('a')
print Solution().minCut('abcdcba')
print Solution().minCut('aabbcdbb')
print Solution().minCut('bb')

