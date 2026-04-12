class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target = sum(nums)//2
        def backtrack(i,total):
            if total == target:
                return True
            if total > target or i >= len(nums):
                return False
            if backtrack(i+1, total+nums[i]):
                return True
            return backtrack(i+1, total)
        
        return backtrack(0,0)