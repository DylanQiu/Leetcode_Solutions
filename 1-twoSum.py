class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        flags = [1 for i in xrange(len(nums))]
        for i in xrange(len(nums)):
            n = target - nums[i]
            flags[i] = 0
            nums[i] = None
            if n in nums and flags[nums.index(n)] ==1:
                return [i, nums.index(n)]
