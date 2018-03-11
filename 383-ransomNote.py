import collections

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        print collections.Counter(ransomNote), (collections.Counter(magazine))
        return not collections.Counter(ransomNote) - (collections.Counter(magazine))

a = Solution()
print a.canConstruct('a', 'b')
