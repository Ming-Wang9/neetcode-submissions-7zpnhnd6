class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1+freq.get(n,0)
        frequence = [[-f,n] for n,f in freq.items()]
        heapq.heapify(frequence)
        res = []
        while k>0:
            f, n = heapq.heappop(frequence)
            res.append(n)
            k-=1
        return res

