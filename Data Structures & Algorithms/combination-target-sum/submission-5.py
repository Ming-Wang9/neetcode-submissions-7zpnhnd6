class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(nums)
        self.res = []
        def backtrack(i,sub,cursum):
            if cursum == target:
                self.res.append(sub.copy())
                return 
            if i == len(nums) or cursum > target:
                return 
            sub.append(nums[i])
            backtrack(i,sub,cursum+nums[i])
            sub.pop()
            backtrack(i+1,sub,cursum)
        backtrack(0,[],0)
        return self.res