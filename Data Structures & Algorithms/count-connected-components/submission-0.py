class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            while n != par[n]:
                par[n] = par[par[n]]
                n = par[n]
            return n 
        
        def union(n1,n2):
            par1, par2= find(n1), find(n2)
            if par1 == par2:
                return 0
            if rank[par1]> rank[par2]:
                par[par2] = par1
                rank[par1] += rank[par2]
            par[par1] = par2
            rank[par2] += rank[par1]
            return 1
        
        res = n 
        for n1,n2 in edges:
            res -= union(n1,n2)
        return res
                




