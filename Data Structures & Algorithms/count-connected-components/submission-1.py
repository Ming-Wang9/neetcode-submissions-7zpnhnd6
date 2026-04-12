class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            while x != par[x]:
                par[x] = par[par[x]]
                x = par[x]
            return x 
        
        def union(x,y):
            rootx, rooty= find(x), find(y)
            if rootx == rooty:
                return 0
            if rank[rootx]> rank[rooty]:
                par[rooty] = rootx
                rank[rootx] += rank[rooty]
            par[rootx] = rooty
            rank[rooty] += rank[rootx]
            return 1
        
        res = n 
        for x,y in edges:
            res -= union(x,y)
        return res
                




