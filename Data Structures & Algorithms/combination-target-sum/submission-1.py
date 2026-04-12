class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, com, total):
            #if the sum of the subset larger than
            #target or out of range, we stop exploring
            if total > target or i >= len(nums):
                return
            #if the sum of subset is equal,
            #add it to the finaly answer
            if total == target:
                res.append(com.copy())
                return 

            #left decision, add itself
            com.append(nums[i])
            dfs(i, com, total+nums[i])
            #right decision, not to add it self
            #move to next number instead
            com.pop()
            dfs(i+1, com, total)

            return res
        return dfs(0, [], 0)