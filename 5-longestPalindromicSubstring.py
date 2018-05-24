class Solution(object):
    def longestPalindrome(self, s):
        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        res = ""
        for i in xrange(len(s)):
            tmp = helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

a = Solution()
print a.longestPalindrome("abaaaa")