class Solution(object):
    def fourSum(self, nums, target):
        """

        :param nums: List[int]
        :return: List[List[int]]
        """
        def findNSum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:
                return
            if N == 2:
                l,r = 0, len(nums)-1
                while l < r:
                    s = nums[l]+nums[r]
                    if s == target:
                        results.append(result+[nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        # while l < r and nums[r] == nums[r-1]:
                        #     r -= 1
                        l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in xrange(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNSum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        results = []
        findNSum(sorted(nums), target, 4, [], results)
        return results








a = Solution()
print a.fourSum([-1, 0, 1, -2, 2, 0], 0)