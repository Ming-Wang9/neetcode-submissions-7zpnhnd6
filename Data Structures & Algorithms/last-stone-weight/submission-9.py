class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for s in stones:
            heapq.heappush(maxheap, -s)
        
        while len(maxheap) > 1:
            x = -heapq.heappop(maxheap)
            y = -heapq.heappop(maxheap)
            if x!=y:
                if x>y:
                    heapq.heappush(maxheap, -(x-y))
                else:
                    heapq.heappush(maxheap,-(y-x))
        return -maxheap[0] if maxheap else 0

