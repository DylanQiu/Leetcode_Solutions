class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0 :
            return False
        l, r = 0, int(c**0.5)
        while l <= r:
            if l**2 + r**2 == c:
                return True
            elif l**2 + r**2 < c:
                l += 1
            else:
                r -= 1
        return False