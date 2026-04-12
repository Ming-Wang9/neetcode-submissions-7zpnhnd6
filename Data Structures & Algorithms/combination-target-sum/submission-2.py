class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]
        def backtrack(i, com, total):
            if total > target or i >= len(nums):
                return
            if total == target:
                res.append(com.copy())
                return
            #add current number
            com.append(nums[i])
            backtrack(i, com, total+nums[i])
            com.pop()
            backtrack(i+1, com, total)
            return res
        return backtrack(0,[],0)