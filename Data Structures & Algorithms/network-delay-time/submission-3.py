class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #djikstra algo
        graph = {i:[] for i in range(1, n+1)}
        for u,v,w in times:
            graph[u].append((v,w))
        minheap =[(0,k)] #time, dst
        visited =set()
        res = 0
        while minheap:
            time, dst = heapq.heappop(minheap)
            if dst in visited:
                continue
            visited.add(dst)
            res = time
            for nei,w in graph[dst]:
                if nei not in visited:
                    heapq.heappush(minheap, (time+w, nei))
        return res if len(visited)==n else -1
