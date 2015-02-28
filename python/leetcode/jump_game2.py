class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A, steps=None):
        if steps == None:
            steps = 0
        if len(A) == 1:
            return steps
        current = A[0]
        possible_step_num = A[0:current]
        max_jump = 0
        for s in possible_step_num:
            if s < len(A):
                max_jump = max(max_jump, s)
        if max_jump == 0:
            return 0
        return self.jump(A[max_jump:], steps + 1)

    def jump2(self, A):
        steps = 0
        last = 0
        current = 0
        for i in range(len(A)):
            print last
            if i > last:
                last = current
                steps += 1
            current = max(current, i+A[i])
            # print current
        return steps



# print Solution().jump([2, 3, 1, 1, 4, 5])
print Solution().jump2([2, 3, 1, 1, 4])
