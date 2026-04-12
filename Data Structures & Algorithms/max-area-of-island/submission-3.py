class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r,c):
            if (r<0 or c<0 or 
                r>= rows or c >= cols or
                (r,c) in visited or
                grid[r][c] != 1):
                return 0
            visited.add((r,c))
            return (1+dfs(r+1, c)+ 
                    dfs(r-1, c)+
                    dfs(r,c+1)+
                    dfs(r,c-1))
        
        maxres = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxres = max(maxres, dfs(r,c))
        return maxres





