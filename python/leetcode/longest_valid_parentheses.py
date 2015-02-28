class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        lastError = -1
        result = 0
        for i in range(0, len(s)):
            if s[i] =='(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    lastError = i;
                else:
                    stack.pop()
                    if len(stack) == 0:
                        validTill = lastError
                    else:
                        validTill = stack[-1]
                    result = max(result, i-validTill)
        return result

print Solution().longestValidParentheses("()(()")
