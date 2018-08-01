class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        if not s or not g:
            return 0
        i, j = 0, 0
        count = 0
        while i < len(g) and j < len(s):
            if g[i] > s[j]:
                j += 1
            else:
                count += 1
                i += 1
                j += 1
        return count

a = Solution()
print a.findContentChildren([10, 9, 8, 7],[5, 6, 7, 8])