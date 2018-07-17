class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        num1, num2 = list(num1), list(num2)
        res = []
        while len(num1)>0 or len(num2)>0:
            tmp1 = ord(num1.pop()) - ord('0') if len(num1)>0 else 0
            tmp2 = ord(num2.pop()) - ord('0') if len(num2)>0 else 0
            c = tmp1 + tmp2 + carry
            carry = c/10
            res.append(c%10)
        if carry:
            res.append(1)
        return ''.join([str(i) for i in res])[::-1]