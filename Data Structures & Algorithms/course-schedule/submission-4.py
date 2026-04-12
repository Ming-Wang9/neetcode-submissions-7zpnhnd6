class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #do dfs, detect cycle
        #pre -> crs
        graph = {i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            graph[p].append(c)
        
        visited = set()
        def dfs(c):
            if graph[c] == []:
                return True
            if c in visited:
                return False
            visited.add(c)
            for nextcrs in graph[c]:
                if not dfs(nextcrs):
                    return False
            #pre may have multiple path to different courses
            visited.remove(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
