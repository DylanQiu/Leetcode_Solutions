class Solution(object):
    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     return self.climbStairs(n-1) + self.climbStairs(n-2)
    #
    # def climbStairs2(self, n):
    #     step_one = 1
    #     step_two = 1
    #     if n == 1:
    #         return step_two
    #     for _ in range(1, n):
    #         step_one, step_two = step_two, step_one + step_two
    #     return step_two

    def __init__(self):
        self.dic = {1:1, 2:2}

    def climbStairs(self, n):
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]


a = Solution()
print a.climbStairs(35)
