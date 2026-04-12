class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
        graph = {i:[] for i in range(n)}
        visit = set()
        for u,v in edges:
            graph[v].append(u)
            graph[u].append(v)

        def dfs (node, par):
            # if there is a cycle, it can't be a valid tree
            if node in visit:
                return False
            visit.add(node)
            for nei in graph[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0,-1) and len(visit) == n