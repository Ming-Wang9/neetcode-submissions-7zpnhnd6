class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        visited = set()

        for c,p in prerequisites:
            graph[c].append(p)

        def dfs(c):
            if c in visited:
                return False
            if graph[c] == []:
                return True
            visited.add(c)
            for p in graph[c]:
                if not dfs(p):
                    return False
            visited.remove(c)
            graph[c] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True