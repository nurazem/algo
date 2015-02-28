class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num, partials=None):
        if partials == None:
            partials = []
        n = len(num)
        if n == 0:
            return []
        if n == 1:
            return num
        if n > 1:
            mid = n / 2
            partials.append(self.permute(num[:mid], partials))
            partials.append(self.permute(num[mid:], partials))
            return partials

    def permuteNaive(self, num):
        result = []
        if len(num) == 1:
            return [num]
        for i in range(len(num)):
            for j in range(len(num)):
                if i!= j:
                    current = list(num)
                    temp = current[i]
                    current[i] = current[j]
                    current[j] = temp
                    print current
                    result.append(current)
        # result.reverse()
        return result


print Solution().permuteNaive([0, 1])

