class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        maxheap = [-n for n in nums]
        heapq.heapify(maxheap)
        res = nums[0]
        while k > 0:
            res = heapq.heappop(maxheap)
            k-=1
        return -res
