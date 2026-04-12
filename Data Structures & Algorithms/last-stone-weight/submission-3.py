class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            fst = heapq.heappop(maxheap)
            scd = heapq.heappop(maxheap)
            heapq.heappush(maxheap, fst-scd)
        return abs(maxheap[0])