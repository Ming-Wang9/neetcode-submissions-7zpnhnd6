class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1+ count.get(n,0)
        minheap = []
        for n in count.keys():
            heapq.heappush(minheap, (count[n], n))
            if len(minheap) > k:
                heapq.heappop(minheap)
        res = []
        while k > 0:
            res.append(heapq.heappop(minheap)[1])
            k-=1
        return res