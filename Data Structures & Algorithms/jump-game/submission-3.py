class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums)-2, -1, -1):
            for step in range(nums[i]+1):
                if i + step < len(nums) and dp[i+step] == True:
                    dp[i] = True
        return dp[0]