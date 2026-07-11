class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for p in points:
            heapq.heappush(minheap,(p[0]**2+p[1]**2, p))
        res = []
        while k>0:
            dis, point = heapq.heappop(minheap)
            res.append([point[0], point[1]])
            k-=1
        return res
