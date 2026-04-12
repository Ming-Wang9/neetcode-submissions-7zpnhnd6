class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for p in points:
            x=p[0]
            y=p[1]
            dist = x**2 +y**2
            minheap.append([dist, x, y])
        heapq.heapify(minheap)
        res = []
        while k >0:
            dist, x, y = heapq.heappop(minheap)
            res.append([x,y])
            k -=1
        return res