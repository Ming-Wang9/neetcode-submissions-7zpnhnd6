class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #dfs, and if detec a cycle then false
        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited =set()
        def dfs (node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0,-1) and len(visited) == n