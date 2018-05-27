class Solution(object):
    def threeSum(self, nums):
        """

        :param nums: List[int]
        :return: List[List[int]]
        """
        nums.sort()
        res = []

        for i in xrange(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            lo = i+1
            hi = len(nums)-1
            while lo < hi:
                tmp = nums[lo] + nums[hi] + nums[i]
                if tmp == 0:
                    res.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif tmp > 0:
                    hi -= 1
                else:
                    lo += 1
        return res




a = Solution()
print a.threeSum([-1, 0, 1, 2, -1, -4])
