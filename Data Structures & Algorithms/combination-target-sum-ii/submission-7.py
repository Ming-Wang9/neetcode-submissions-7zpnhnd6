class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates)<target:
            return []
        candidates = sorted(candidates)
        self.res = []
        def backtrack(i,sub,total):
            if total == target:
                self.res.append(sub.copy())
                return
            if i == len(candidates) or total > target:
                return
            sub.append(candidates[i])
            backtrack(i+1,sub,total+candidates[i])
            sub.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            backtrack(i+1,sub,total)
        backtrack(0,[],0)
        return self.res