class Solution(object):
    def containsDuplicate(self, nums):
        """
        find if the array contains any duplicates.
        :param nums: List[int]
        :return: bool
        """
        if len(nums) == 0:
            return False
        for i in xrange(len(nums)):
            if nums.count(nums[i]) != 1:
                return True
        return False