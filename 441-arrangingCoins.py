class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=0:
            return 0
        rowLen, res = 1, 0
        while n>0:

            n -= rowLen
            if n < 0:
                break
            rowLen += 1
            res += 1
        return res