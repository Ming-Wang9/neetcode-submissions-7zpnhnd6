class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            s1=-heapq.heappop(maxheap)
            s2=-heapq.heappop(maxheap)
            diff = s1-s2
            if diff != 0:
               heapq.heappush(maxheap, -diff)
        return -maxheap[0] if maxheap else 0

