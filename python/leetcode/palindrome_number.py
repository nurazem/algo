class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        len_x = 1
        temp = x
        if x < 0:
            return False
        while temp / (10 ** len_x) != 0:
            len_x += 1

        l = len_x / 2
        rem = x % (10 ** l)
        lead = x / (10 ** (l+ 1))
        print rem
        print lead
        return rem == lead


print Solution().isPalindrome(12321)
