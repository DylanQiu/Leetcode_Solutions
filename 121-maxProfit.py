class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        lowest = prices[0]
        profit = 0
        for price in prices:
            if price < lowest:
                lowest = price
            elif profit < price - lowest:
                profit = price - lowest
        return profit
