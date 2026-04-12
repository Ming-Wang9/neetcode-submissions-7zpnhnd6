class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def backtrack(path):
            if len(path) == len(nums):
                self.res.append(path.copy())
                return 
            for n in nums:
                if n not in path:
                    path.append(n)
                    backtrack(path)
                    path.pop()
        backtrack([])
        return self.res
