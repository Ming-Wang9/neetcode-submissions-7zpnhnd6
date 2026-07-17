class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q= deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append([r,c])
        directions =[[1,0], [-1,0], [0,1], [0,-1]]
        time = 0
        while q and fresh:
            for _ in range(len(q)):
                row,col = q.popleft()
                for nr, nc in directions:
                    newrow,newcol = row+nr, col+nc
                    if (newrow<0 or newcol<0 or
                        newrow>=rows or newcol>=cols or
                        grid[newrow][newcol]!=1):
                        continue
                    grid[newrow][newcol]=2
                    q.append([newrow, newcol])
                    fresh-=1
            time+=1
        return time if fresh == 0 else -1



