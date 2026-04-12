class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows,cols = len(matrix), len(matrix[0])
        dp = [[0]*cols for _ in range(rows)]
        def dfs(r,c,prev):
            if (r<0 or c<0 or 
                r>=rows or c>=cols or 
                matrix[r][c]<=prev):
                return 0
            if dp[r][c]!= 0:
                return dp[r][c]
            res = 1
            res=max(res, 1+dfs(r+1,c,matrix[r][c]))
            res=max(res, 1+dfs(r-1,c,matrix[r][c]))
            res=max(res, 1+dfs(r,c+1,matrix[r][c]))
            res=max(res, 1+dfs(r,c-1,matrix[r][c]))
            dp[r][c] = res
            return res
        maxres = 0
        for r in range(rows):
            for c in range(cols):
                maxres = max(maxres, dfs(r,c,-1))
        return maxres