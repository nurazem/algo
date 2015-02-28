# class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    # def wordBreak(self, s, dict):
    #     if s in dict:
    #         return True
    #     else:
    #         i = 0
    #         current = ""
    #         while i < len(s):
    #             current += s[i]
    #             # print current
    #             if current in dict:
    #                 for j in range(len(dict)):
    #                     if self.startsWith(current, dict[j]):
    #                         dict[j] = dict[j][len(current):]
    #                     print dict
    #                 print
    #                 print s[i+1:]
    #                 return self.wordBreak(s[i+1:], dict)
    #             i += 1
    #         return False

    # def startsWith(self, source, target):
    #     if len(source) > len(target):
    #         return False
    #     for i in range(len(source)):
    #         if source[i] != target[i]:
    #             return False
    #     return True

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        segmented = [True];
        for i in range (0, len(s)):
            segmented.append(False)
            for j in range(i,-1,-1):
                if segmented[j] and s[j:i+1] in dict:
                    segmented[i+1] = True
                    break
        print segmented
        return segmented[len(s)]


print Solution().wordBreak("goalspecial", ["go","goal","goals","special"])
# print Solution().wordBreak("leetcode", ["leet","code"])
