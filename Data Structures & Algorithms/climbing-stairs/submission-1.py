class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n 
        # after the first two steps, every step after it either take 1 or 2
        # so it is reuse the resulet from previous steps
        dp =[0] * (n+1) # since need to reach the top, one step after last step
        dp[1], dp[2] = 1,2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

