class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = [[x**2+y**2,x,y] for x,y in points]
        heapq.heapify(minheap)
        res = []
        while k > 0:
            dis,x,y = heapq.heappop(minheap)
            res.append([x,y])
            k-=1
        return res
