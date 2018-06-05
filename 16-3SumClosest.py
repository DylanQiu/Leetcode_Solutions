import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = sys.maxint

        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while r>l:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == target:
                    return target
                if tmp > target:
                    r -= 1
                else:
                    l += 1
                if abs(tmp-target)<abs(result-target):
                    result = tmp
        return result



a = Solution()
print a.threeSumClosest([0,1,2], 3)