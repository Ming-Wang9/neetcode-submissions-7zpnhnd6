class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {n:[] for n in range(numCourses)}
        for c, p in prerequisites:
            graph[p].append(c)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if course == numCourses:
                return True
            visited.add(course)
            for nxt in graph[course]:
                if not dfs(nxt):
                    return False
            visited.remove(course)
            graph[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True