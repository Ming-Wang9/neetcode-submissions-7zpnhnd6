class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            graph[c].append(p)
        res =[]
        visit, cycle = set(), set()
        def dfs (c):
            if c in cycle:
                return False
            if c in visit:
                return True
            cycle.add(c)
            for p in graph[c]:
                if dfs(p) == False:
                    return False
            cycle.remove(c)
            visit.add(c)
            res.append(c)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res