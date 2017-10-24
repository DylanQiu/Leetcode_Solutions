class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        div = 1
        while (x /div >= 10):
            div = div*10

        while (x != 0):
            if x%10 != x/div:
                return False
            x = (x % div)/10
            div = div/100
        return True


a = Solution()
a.isPalindrome(1000)
