class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buylow = prices[0]
        for p in prices:
            profit = max(profit,  p - buylow)
            buylow = min(buylow, p)
        return profit 
