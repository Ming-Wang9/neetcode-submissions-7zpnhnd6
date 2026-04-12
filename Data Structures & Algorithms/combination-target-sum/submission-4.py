class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res =[]
        def backtrack(i,path):
            if sum(path) == target:
                self.res.append(path.copy())
                return
            if sum(path)>target or i > len(nums)-1:
                return 
            path.append(nums[i])
            backtrack(i, path)
            path.pop()
            backtrack(i+1,path)
            return self.res
        backtrack(0,[])
        return self.res