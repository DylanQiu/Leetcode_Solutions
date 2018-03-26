class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :param s: str
        :param t: str
        :return: bool
        """
        if len(s) == 0:
            return True
        l1 = []
        l2 = []
        for i in xrange(len(s)):
            if s[i] not in l1 and t[i] not in l2:
                l1.append(s[i])
                l2.append(t[i])
                continue
            if s[i] in l1 and t[i] in l2:
                if l1.index(s[i]) == l2.index(t[i]):
                    continue
                else:
                    return False
            else:
                return False
        return True