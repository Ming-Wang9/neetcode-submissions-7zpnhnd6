class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        direction =[[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c,prev):
            if (r<0 or c<0 or
                r>=rows or c>=cols or
                matrix[r][c] <= prev):
                return 0
            lenpath = 0
            for d in direction:
                lenpath = max(lenpath, 1+dfs(r+d[0], c+d[1], matrix[r][c]))
            return lenpath
        res = 0
        for r in range(rows):
            for c in range(cols):
                res= max(res,dfs(r,c, -1))
        return res
        