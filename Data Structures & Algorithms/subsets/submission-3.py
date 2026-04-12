class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res =[]
        def backtrack(i, sub):
            if i == len(nums):
                self.res.append(sub.copy())
                return
            sub.append(nums[i])
            backtrack(i+1,sub)
            sub.pop()
            backtrack(i+1,sub)
            return self.res
        backtrack(0,[])
        return self.res