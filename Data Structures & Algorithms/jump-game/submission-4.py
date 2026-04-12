class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # # i am so pround that is my first time
        # # solve a dp by myself!
        # dp = [False] * len(nums)
        # dp[-1] = True
        # for i in range(len(nums)-2, -1, -1):
        #     for step in range(nums[i]+1):
        #         if i + step < len(nums) and dp[i+step] == True:
        #             dp[i] = True
        # return dp[0]

        #greedy
        goal = len(nums)-1
        for i in range(goal-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal==0
