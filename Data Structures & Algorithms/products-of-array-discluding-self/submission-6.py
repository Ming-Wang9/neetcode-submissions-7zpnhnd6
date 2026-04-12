class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        pro = [1] * len(nums)
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            pro[i] = pro[i+1] * nums[i+1]
        res = []
        for i in range(len(nums)):
            res.append(pre[i]*pro[i])
        return res
        
        
