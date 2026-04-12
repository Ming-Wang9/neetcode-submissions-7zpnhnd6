class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(i,sub,total):
            if total == target:
                res.append(sub.copy())
                return 
            if total > target or i >n-1:
                return 
            sub.append(nums[i])
            backtrack(i,sub,total+nums[i])
            sub.pop()
            backtrack(i+1, sub, total)
            return res
        return backtrack(0,[],0)