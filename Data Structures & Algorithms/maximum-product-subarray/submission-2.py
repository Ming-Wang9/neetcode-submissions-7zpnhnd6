class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp , minp = 1, 1
        res = max(nums)
        for n in nums:
            if n == 0:
                maxp, minp = 1, 1
                continue
            temp = maxp*n
            maxp = max(n*maxp, n*minp, n)
            minp = min(temp, n*minp, n)
            res = max(res, maxp)
        return res


        