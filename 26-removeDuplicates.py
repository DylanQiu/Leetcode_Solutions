class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        count = 0
        for i in xrange(1, len(nums)):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]

        return count + 1
