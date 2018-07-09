class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        if num == 1 or num==0:
            return True
        l, u = 1, num
        while l**2 < num < u**2:
            mid = (l+u)/2
            if mid**2 <= num <= (mid+1)**2:
                break
            if (mid+1)**2 < num:
                l = mid+1
            if num < mid**2:
                u = mid

        return mid*mid == num or (mid+1)**2 == num

a = Solution()
print a.isPerfectSquare(81)