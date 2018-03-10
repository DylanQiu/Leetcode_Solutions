class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last+i, now)
        return now


a = Solution()
print a.rob([1,2,3,4,5,6])
