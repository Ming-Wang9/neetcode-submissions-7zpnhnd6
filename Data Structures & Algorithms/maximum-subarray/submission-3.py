class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp question???
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            # to have max, either start with it self
            # or add its previous too
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        return max(dp)
        