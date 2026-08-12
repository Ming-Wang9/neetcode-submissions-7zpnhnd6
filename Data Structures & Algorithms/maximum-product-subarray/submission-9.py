class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        posdp = [1] * n
        negdp = [1] * n
        posdp[0] = negdp[0] = nums[0]
        res = nums[0]
        for i in range(1, n):
            posdp[i] = max(nums[i], nums[i]*posdp[i-1], nums[i]*negdp[i-1])
            negdp[i] = min(nums[i], nums[i]*posdp[i-1], nums[i]*negdp[i-1])
            res = max(res,posdp[i],negdp[i])
        return res
