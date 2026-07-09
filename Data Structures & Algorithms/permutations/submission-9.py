class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        self.res = []
        def backtrack(sub):
            if len(sub)==len(nums):
                self.res.append(sub.copy())
                return 
            for n in nums:
                if n not in sub:
                    sub.append(n)
                    backtrack(sub)
                    sub.pop()
        backtrack([])
        return self.res