class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #sort it to avoid duplicate, then backtracking for subset
        nums.sort()
        res= []
        def backtrack(i,subset):
            if i == len(nums):
                return res.append(subset.copy())
            #include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()
            #exclude nums[i]
            while i + 1< len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1, subset)     
        backtrack(0,[])
        return res       