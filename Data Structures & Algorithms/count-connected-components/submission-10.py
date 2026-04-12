class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #dfs in graph
        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res +=1
        return res