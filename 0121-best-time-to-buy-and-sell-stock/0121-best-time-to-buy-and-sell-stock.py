class Solution(object):
    def maxProfit(self, prices):
        minimum = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            if prices[i]>minimum:
                profit = max(profit, prices[i] - minimum)
        return profit

        """
        :type prices: List[int]
        :rtype: int
        """
        