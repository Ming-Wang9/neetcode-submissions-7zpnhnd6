class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmin, curmax = 1,1
        for n in nums:
            temp = n * curmax
            curmax = max(n * curmax, n *curmin, n)
            curmin = min(temp, n*curmin, n)
            res = max(res, curmax)
        return res