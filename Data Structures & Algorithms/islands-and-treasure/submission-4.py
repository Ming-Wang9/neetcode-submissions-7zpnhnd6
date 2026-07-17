class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2**31-1
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q:
            row, col = q.popleft()
            for r, c in directions:
                newrow, newcol = row+r, col+c
                if (newrow<0 or newcol<0 or
                    newrow>=rows or newcol>=cols or
                    grid[newrow][newcol] != INF):
                    continue
                grid[newrow][newcol] = grid[row][col]+1
                q.append([newrow,newcol])


