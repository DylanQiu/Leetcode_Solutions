class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return (1)

        nums = sorted(nums)
        for i in range(1, len(nums) + 1):
            if (i not in nums):
                i = i - 1
                break
        return (i + 1)