INT32_MAX = (2**31)-1
INT32_MIN = (-1)*(2**31)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > INT32_MAX or x < INT32_MIN or x == 0:
            return 0
        num = str(abs(x))
        b = ''
        for i in num[::-1]:
            b += i
        b = int(b)
        if b > INT32_MAX or b < INT32_MIN:
            return 0
        flag = x/abs(x)
        return flag * b
