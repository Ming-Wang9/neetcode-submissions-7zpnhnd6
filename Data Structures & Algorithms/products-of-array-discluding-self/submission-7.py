class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*n
        pro = [1]*n
        for i in range(1,n):
            # if i > 0:
            pre[i] = nums[i-1]*pre[i-1]
        for j in range(n-2,-1,-1):
            # if j<n:
            pro[j] = nums[j+1]*pro[j+1]
        res = [1]*n
        for idx in range(n):
            res[idx] = pre[idx]*pro[idx]
        return res