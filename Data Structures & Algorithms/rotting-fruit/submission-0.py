class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        time = 0

        # adding all rootten fruit to deque
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1
        
        # start to do bfs on rotten fruit (recursively)
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                # move to one of the directions
                for dr, dc in direction:
                    row, col = r+dr, c+dc
                    if (row<0 or col<0 or 
                        row >= rows or col >= cols or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append((row,col))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
                

        







