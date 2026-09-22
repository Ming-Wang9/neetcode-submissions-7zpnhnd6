class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = {}
        for n in nums:
            numdict[n] = 1+numdict.get(n,0)
        heap = []
        for n in numdict.keys():
            heapq.heappush(heap,(numdict[n], n))
            if len(heap)>k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
