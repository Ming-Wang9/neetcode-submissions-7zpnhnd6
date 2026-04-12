class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path):
            # base case: one permutation found
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num not in path:    # skip already used numbers
                    path.append(num)
                    backtrack(path)
                    path.pop()         # undo the choice

        backtrack([])
        return res