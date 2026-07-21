class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights), len(heights[0])
        def dfs(r,c,prev,visited):
            if (r<0 or c<0 or
                r>=rows or c>=cols or
                heights[r][c]<prev or
                (r,c) in visited):
                return 
            prev = heights[r][c]
            visited.add((r,c))
            dfs(r+1,c,prev,visited)
            dfs(r-1,c,prev,visited)
            dfs(r,c+1,prev,visited)
            dfs(r,c-1,prev,visited)

        pacset, atlset=set(), set()
        for r in range(rows):
            dfs(r,0,0,pacset)
            dfs(r, cols-1,0, atlset)
        for c in range(cols):
            dfs(0,c,0,pacset)
            dfs(rows-1,c,0,atlset)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacset and (r,c) in atlset:
                    res.append([r,c])
        return res

        
