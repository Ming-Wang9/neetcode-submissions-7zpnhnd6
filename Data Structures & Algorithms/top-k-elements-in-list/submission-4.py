class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #have a hashtable to record the count of nums
        # in a while loop, while k > 0:
        # keep find the max count and then return the key
        # append the key to res utill k = 0
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        heap = [(-c, n) for n, c in count.items()]
        heapq.heapify(heap)
        res = []
        while k > 0:
            num = heapq.heappop(heap)
            res.append(num[1])
            k -=1
        return res
