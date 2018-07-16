class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd = []
        for i in s:
            if i not in odd:
                odd.insert(0, i)
            else:
                odd.remove(i)
        if odd == []:
            return len(s)
        return len(s) - len(odd) + 1