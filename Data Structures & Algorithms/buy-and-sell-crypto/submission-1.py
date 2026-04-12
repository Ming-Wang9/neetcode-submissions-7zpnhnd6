class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        buy_low = float("inf")
        for price in prices:
            if price < buy_low:
                buy_low = price
            if price - buy_low > diff:
                diff = price - buy_low
        return diff