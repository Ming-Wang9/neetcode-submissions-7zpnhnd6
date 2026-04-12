class Solution:
    def climbStairs(self, n: int) -> int:
        # think about the top to down dp
        # to reach the end of last integer
        # either take one step from the closest one
        # or take two staps from the second closest one
        dp = [0] * (n+1)
        if n <= 2:
            return n
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

