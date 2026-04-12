class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # do dfs 
        rows, cols = len(grid), len(grid[0])
        visited = set()
        self.res = 0
        def dfs(r,c):
            #base case
            if (r<0 or c<0 or
                r >=rows or c>=cols or
                (r,c) in visited or 
                grid[r][c] != 1):
                return 0
            visited.add((r,c))
            self.res =1
            self.res += dfs(r+1,c)
            self.res += dfs(r-1,c)
            self.res += dfs(r,c+1)
            self.res += dfs(r,c-1)
            return self.res

        self.maxres = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    self.maxres = max(self.maxres, dfs(r,c))
        return self.maxres