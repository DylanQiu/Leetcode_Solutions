class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # if not s:
        #     return False
        # l = len(s)
        # for i in range(1, l/2+1)[::-1]:
        #     if l%i == 0:
        #         subS = s[:i]
        #         sb = ''
        #         m = l/i
        #         for j in range(l/i):
        #             sb += subS
        #         if sb == s:
        #             return True
        # return False
        if not s:
            return False
        ss = (s+s)[1:-1]
        return ss.find(s) != -1


a = Solution()
print a.repeatedSubstringPattern("abab")