class Solution:
    def combine(self, n, k, current=None, i=None):
        if current == None: current = []
        if i == None: i = 1
        if k == 0:
            return [current]
        if i > n:
            return []
        print i
        return self.combine(n, k, current, i + 1) + self.combine(n, k - 1, current + [i], i + 1)

print Solution().combine(4, 3)
