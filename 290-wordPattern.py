class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        l1, l2 = list(pattern), str.split()
        for i in xrange(len(l1)):
            if l1.index(l1[i]) != l2.index(l2[i]):
                return False
        return True