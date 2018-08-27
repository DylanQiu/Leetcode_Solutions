import collections


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return sum(v>1 for v in collections.Counter(nums).values())
        elif k > 0:
            return len(set(nums)&set(n+k for n in nums))
        else:
            return 0

a = Solution()
print a.findPairs([1,3,1,5,4],0)