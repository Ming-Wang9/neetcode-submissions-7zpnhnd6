class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buylow = float('inf')
        for p in prices:
            if p > buylow:
                profit = max(profit,p-buylow)
            buylow= min(buylow,p)
        return profit