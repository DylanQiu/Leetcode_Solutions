class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (num > 0) and (num==1 or (num%4==0 and self.isPowerOfFour(num/4)))