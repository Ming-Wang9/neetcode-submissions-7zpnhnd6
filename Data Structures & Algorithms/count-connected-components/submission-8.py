class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #do dfs on the node, then +1 if reach end
        
        #build the graph
        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        res =0
        def dfs(node):
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        for node in range(n):
            if not visited[node]:
                visited[node]= True
                dfs(node)
                res+=1
        return res

            







        