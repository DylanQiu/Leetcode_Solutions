# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    return 1
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi )/2
            if guess(mid) == 1:
                lo = mid+1
            else:
                hi = mid
        return lo