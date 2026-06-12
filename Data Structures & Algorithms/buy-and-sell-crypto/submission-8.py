class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = prices[0]
        profit = 0
        for p in prices:
            profit = max(profit, p-buy)
            buy = min(buy, p)
        return profit