class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        res = [1] * n
        for i in range(1,n):
            prefix[i] = nums[i-1]*prefix[i-1]
        for j in range(n-2, -1,-1):
            suffix[j] = nums[j+1]*suffix[j+1]
        for k in range(n):
            res[k] = prefix[k]*suffix[k]
        return res