class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset= []
        def dfs(i):
            #base case
            if i >= len(nums):
                res.append(subset.copy())
                return 
            # if add the n to the subset
            # do recursive search for it
            subset.append(nums[i])
            dfs(i+1)
            #if not to add it, do recursive serch for it too
            subset.pop()
            dfs(i+1)
            return res
        return dfs(0)
