class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols= len(grid), len(grid[0])
        visited = set()
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while q:
            row, col = q.popleft()
            for r,c in directions:
                newr,newc = row+r, col+c
                if (newr<0 or newc<0 or 
                    newr>=rows or newc>=cols or
                    grid[newr][newc] != 2**31-1 or 
                    (newr, newc) in visited):
                    continue
                grid[newr][newc] = grid[row][col]+1
                visited.add((newr,newc))
                q.append([newr,newc])