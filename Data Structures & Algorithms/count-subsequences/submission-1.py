class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t)>len(s):
            return 0
        dp = {}
        def backtrack(i,j):
            if j == len(t):
                return 1
            if i ==len(s):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if s[i]==t[j]:
                dp[(i,j)] = backtrack(i+1,j+1) + backtrack(i+1,j)
            else:
                dp[(i,j)] = backtrack(i+1,j)
            return dp[(i,j)]
        return backtrack(0,0)

