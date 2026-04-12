class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            graph[pre].append(crs)
        visited = set()
        def dfs(c):
            if c in visited:
                return False
            if graph[c] == []:
                return True
            visited.add(c)
            for nxt in graph[c]:
                if not dfs(nxt):
                    return False
            visited.remove(c)
            graph[c] = []
            return True 
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

            
