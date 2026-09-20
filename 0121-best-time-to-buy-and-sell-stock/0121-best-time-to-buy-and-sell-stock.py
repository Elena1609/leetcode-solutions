class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maximum = prices[0]
        minimum = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - minimum)
            minimum = min(minimum, prices[i])        

        return profit