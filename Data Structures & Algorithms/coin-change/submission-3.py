class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # impossible the amount will need amount+1 coins to make the goal
        # amount +1 because I include 0

        minCoin = [amount +1] * (amount+1)
        minCoin[0] = 0

        # now updated the each impossibe amount to min amount

        for a in range(1, amount+1):
            for c in coins:
                if a-c >=0:
                    minCoin[a] = min(minCoin[a],  1+minCoin[a-c])
        return minCoin[amount] if minCoin[amount] != amount+1 else -1
