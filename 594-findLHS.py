from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numDic = Counter(nums)
        return max([numDic[i] + numDic[i+1] for i in numDic if i+1 in numDic] or [0])