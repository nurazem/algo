class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S, partial=None):
        if partial is None:
            partial = [[]]
        result = []
        print partial
        if len(S) > 0:
            e = S[0]
            S = S[1:]
            for i in range(len(partial)):
                partial.append(partial[i] + [e])
            self.subsets(S, partial)
        return partial

s = Solution()
print s.subsets([1, 2])
