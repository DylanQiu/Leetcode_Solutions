from itertools import permutations

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # ans = []
        # for i in permutations(nums):
        #     ans.append(list(i))
        # return ans
        res = []

        def dfs(num, path, res):
            if not num:
                res.append(path)
            for i in xrange(len(num)):
                dfs(num[:i] + num[i+1:], path+[num[i]], res)
        dfs(nums, [], res)
        return res

a = Solution()
print a.permute([1,2,3])