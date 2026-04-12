class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(1,len(edges)+1)}
        def dfs(src, target, visited):
            if src == target:
                return True
            visited.add(src)
            for nei in graph[src]:
                if nei not in visited and dfs(nei, target, visited):
                    return True
            return False
        for u,v in edges:
            if dfs(u,v,set()):
                return [u,v]
            graph[u].append(v)
            graph[v].append(u)