class Solution:
    # @return an integer
    def reverse(self, x):
        length = 1
        while x / (10 ** length) != 0:
            length += 1
        for i in range((length / 2) + 1):
            rem = x % (10 ** i)
            x = x / (10 ** i)
            x = rem * (10 ** (length - i)) + x

        return x
s = Solution()
print s.reverse(123)
