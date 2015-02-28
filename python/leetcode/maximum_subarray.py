class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A)==0:
            return 0;
        temp = 0;
        maxSum = A[0]
        for i in range(0, len(A)):
            temp = max(A[i], A[i]+temp)
            if temp > maxSum:
                maxSum = temp
        return maxSum

s = Solution()
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
