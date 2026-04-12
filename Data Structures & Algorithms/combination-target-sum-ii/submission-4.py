class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        def backtrack(i, path, total):
            if total == target:
                self.res.append(path.copy())
                return
            if total>target or i >len(candidates)-1:
                return
            path.append(candidates[i])
            backtrack(i+1,path, total+candidates[i])
            path.pop()
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1,path, total)
            return self.res
        backtrack(0,[],0)
        return self.res