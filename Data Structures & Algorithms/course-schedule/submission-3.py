class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #build a graph and then detect if there is a cycle in the graph
        graph = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            graph[p].append(c)
        visited =set()
        def dfs (c):
            #base case
            if graph[c] == []:
                return True
            if c in visited:
                return False
            
            visited.add(c)
            for nextc in graph[c]:
                if not dfs(nextc):
                    return False
            visited.remove(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
            
            
            