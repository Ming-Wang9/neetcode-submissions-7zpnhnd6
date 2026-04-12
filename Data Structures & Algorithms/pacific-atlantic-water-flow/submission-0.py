class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols =  len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs (r,c,visit, prev):
            if (r<0 or c<0 or
                r>=rows or c>= cols or
                (r,c) in visit or
                heights[r][c] < prev):
                return 
            visit.add((r,c))
            dfs(r-1,c,visit,heights[r][c])
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])

        #cell that can have water from pacific or altantic
        for c in range(cols):
            dfs(0,c, pac, heights[0][c]) #top side have pac
            dfs(rows-1, c, atl, heights[rows-1][c])# buttom sider have atl

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0]) #left side, pac
            dfs(r, cols -1, atl, heights[r][cols-1]) #right side, atl
        
        # check if the cell is in both ocean set
        res =[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res