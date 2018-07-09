class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letter if s.count(l)==1]
        return min(index) if len(index)>0 else -1