class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height)-1
        maxC = (j-i)*min(height[i], height[j])

        while i<j:
            h = min(height[i], height[j])
            maxC = max(maxC, h*(j-i))

            while height[i] <= h and i < j:
                i += 1
            while height[j] <= h and i < j:
                j -= 1
        return maxC

a = Solution()
a.maxArea([1,1])