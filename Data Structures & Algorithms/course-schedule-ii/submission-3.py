class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree =[0] * numCourses
        graph = {i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            graph[p].append(c)
            indegree[c] +=1
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []
        while q:
            crs = q.popleft()
            res.append(crs)
            for nxt in graph.get(crs,[]):
                indegree[nxt] -=1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return res if len(res) == numCourses else []