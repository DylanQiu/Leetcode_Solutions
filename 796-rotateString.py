class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a_l = list(A)
        b_l = list(B)
        for i in range(1, len(A)+1):
            print i
            print self.rotate(b_l, i)
            if b_l == self.rotate(a_l, i):
                return True
        return False

    def rotate(self, l, n):
        return l[n:] + l[:n]


a = Solution()
print a.rotateString('abcde', 'abced')