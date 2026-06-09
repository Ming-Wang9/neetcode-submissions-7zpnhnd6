class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1+count.get(n,0)
        maxheap = []
        heapq.heapify(maxheap)
        for num, cnt in count.items():
            heapq.heappush(maxheap,(-cnt, num))
        res = []
        while k > 0:
            cnt,num = heapq.heappop(maxheap)
            res.append(num)
            k-=1
        return res

