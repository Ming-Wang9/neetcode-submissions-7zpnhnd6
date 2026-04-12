class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # n = len(nums)
        # dp = [False] * n
        # dp[-1] = True
        # for i in range(n-2,-1,-1):
        #     for step in range(nums[i]+1):
        #         if i + step < n and dp[i+step] == True:
        #             dp[i] = True
        # return dp[0]
        #
        #greedy version
        #
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0








