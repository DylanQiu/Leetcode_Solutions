class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last1, now1 = 0, 0
        last2, now2 = 0, 0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)-1):
            last1, now1 = now1, max(last1+nums[i], now1)
        for i in range(1, len(nums)):
            last2, now2 = now2, max(last2+nums[i], now2)
        return max(now1, now2)


a = Solution()
print a.rob([1,2,3,4,5,6])
