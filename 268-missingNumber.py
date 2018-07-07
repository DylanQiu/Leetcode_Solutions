class Solution(object):
    def missingNumber(self, nums):
        """

        :param nums: List[int]
        :return: int
        """
        res = len(nums)
        for i in range(len(nums)):
            res = res^i^nums[i]
        return res