class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #too much edges, a graph but not a tree
        if len(edges) != n-1:
            return False
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        #dfs on the node, to detect cycle and see if they are equal
        visited = set()
        def dfs (node, parent):
            if node in visited:
                return False
            visited.add(node)

            for nei in graph[node]:
                #skip itself
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0,-1) and len(visited) == n
        





