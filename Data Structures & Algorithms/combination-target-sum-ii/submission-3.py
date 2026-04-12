class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n=len(candidates)
        res =[]
        def backtrack(i,sub,total):
            if total == target:
                res.append(sub.copy())
                return 
            if total>target or i>n-1:
                return 
            sub.append(candidates[i])
            backtrack(i+1,sub,total+candidates[i])
            sub.pop()
            while i+1 < n and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, sub, total)
            return res
        return backtrack(0,[],0)