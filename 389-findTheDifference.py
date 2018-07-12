class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for i in t:
            if dic.get(i, 0) == 0:
                return i
            else:
                dic[i] -= 1