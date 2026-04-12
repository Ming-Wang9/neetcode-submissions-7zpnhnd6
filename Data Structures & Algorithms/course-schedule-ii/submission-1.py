class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res =[]
        #use topological sort
        indegree = [0] * numCourses
        #build the graph, and record the indegree
        graph={i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            graph[p].append(c)
            indegree[c] += 1
        # starting from a class does ask for any prerequist
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        while q:
            crs = q.popleft()
            res.append(crs)
            for nextc in graph.get(crs, []):
                indegree[nextc] -= 1
                if indegree[nextc] == 0:
                    q.append(nextc)
        return res if len(res) == numCourses else []

            
